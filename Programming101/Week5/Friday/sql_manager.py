import sqlite3
import hashlib
from Client import Client
import time
import random
import smtplib
import email_sender
import binascii
import os


minimum_password_length = 8
special_symbols = "!@#$%^&*()-_=+/<>.,?\\|"
maximum_bad_logins = 4
minimum_bad_logins = 0
login_cooldown = 300.0
number_of_otp = 10

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()
conn.row_factory = sqlite3.Row


def create_clients_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS
        clients (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        balance REAL DEFAULT 0,
        message TEXT,
        email TEXT)''')


def create_credentials_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS
        credentials (id INTEGER PRIMARY KEY,
        bad_logins INTEGER,
        time REAL)""")


def create_otp_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS
        otps (id INTEGER, otp TEXT)""")


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def check_password_strength(username, password):
    return (any(character.islower() for character in password) and
            any(character.isupper() for character in password) and
            any(character.isdigit() for character in password) and
            any(character in special_symbols for character in password) and
            len(password) >= minimum_password_length and
            str(username) not in password)


def change_pass(new_pass, logged_user):
    if check_password_strength(logged_user, new_pass):
        hashpass = hashlib.sha1(new_pass.encode('utf-8')).hexdigest()

        update_sql = "UPDATE clients SET password = ? WHERE id = ?"
        if type(logged_user) == str:
            cursor.execute(update_sql, (hashpass, get_user_id(logged_user)))
        else:
            cursor.execute(update_sql, (hashpass, logged_user.get_id()))
        conn.commit()
        return "Password updated."
    else:
        return "Please enter a valid password."


def register(username, password, email):
    if check_password_strength(username, password):
        hashpass = hashlib.sha1(password.encode('utf-8')).hexdigest()
        insert_sql = "INSERT INTO clients (username, password, email) VALUES (?,?,?)"
        cursor.execute(insert_sql, (username, hashpass, email))
        cursor.execute("SELECT id FROM clients WHERE username = ?", (username,))
        user_id = cursor.fetchone()

        cursor.execute("""INSERT INTO credentials (id, bad_logins)
            VALUES (?,?)""", (user_id[0], minimum_bad_logins))
        conn.commit()
        return "Registration successful."
    else:
        return "Please enter a valid password."


def get_user_id(username):
    cursor.execute("SELECT id FROM clients WHERE username = ?", (username,))
    user_id = cursor.fetchone()
    return user_id[0]


def get_bad_logins(username):
    cursor.execute("""SELECT bad_logins
        FROM credentials INNER JOIN clients
        ON credentials.id = clients.id
        WHERE clients.username = ?""", (username,))
    bad_logins = cursor.fetchone()
    return bad_logins[0]


def increment_bad_logins(username):
    user_id = get_user_id(username)
    bad_logs = get_bad_logins(username)
    if bad_logs <= maximum_bad_logins:
        cursor.execute("UPDATE credentials SET bad_logins = ? WHERE id = ?", (bad_logs+1, user_id))
        conn.commit()


def fifth_failed_login(username):
    ID = get_user_id(username)
    time_of_fail = time.time()
    cursor.execute("UPDATE credentials SET time = ? WHERE id = ?", (time_of_fail, ID))
    conn.commit()
    increment_bad_logins(username)


def clear_login_attempts(username):
    ID = get_user_id(username)
    cursor.execute("UPDATE credentials SET bad_logins = ? WHERE id = ?", (minimum_bad_logins, ID))
    conn.commit()


def get_lock_time(username):
    ID = get_user_id(username)
    cursor.execute("SELECT time FROM credentials WHERE id = ?", (ID,))
    lock_time = cursor.fetchone()
    return lock_time[0]


def check_if_username_exists(username):
    cursor.execute("SELECT username FROM clients")
    result = cursor.fetchall()
    usernames = []
    for row in result:
        usernames.append(row)
    usernames = ["%s" % x for x in usernames]
    if username in usernames:
        return True
    return False


def login(username, password):
    if not check_if_username_exists(username):
        print("Invalid username/password.")
        return False

    current_time = time.time()
    bad_logins = get_bad_logins(username)
    if bad_logins > maximum_bad_logins:
        lock_time = get_lock_time(username)
        if current_time < lock_time + login_cooldown:
            print("You can not login for another {:.2d} seconds."
                  .format(lock_time + login_cooldown - current_time))
            return False
        else:
            clear_login_attempts(username)
            login(username, password)

    if bad_logins < maximum_bad_logins:
        hashpasscheck = hashlib.sha1(password.encode('utf-8')).hexdigest()

        select_query = """SELECT id, username, balance, message, email FROM clients
        WHERE username = ? AND password = ? LIMIT 1"""
        cursor.execute(select_query, (username, hashpasscheck))
        user = cursor.fetchone()
        if(user):
            clear_login_attempts(username)
            return Client(user[0], user[1], user[2], user[3], user[4])
        else:
            increment_bad_logins(username)
            return False
    elif bad_logins == maximum_bad_logins:
        fifth_failed_login(username)


def generate_random_hash():
    hash_numbers = random.getrandbits(128)
    return "{:32x}".format(hash_numbers)


def check_if_hashes_match(username, hash_from_email):
    cursor.execute("SELECT password FROM clients WHERE username = ?", (username,))
    actual = cursor.fetchone()
    if hashlib.sha1(hash_from_email.encode('utf-8')).hexdigest() == actual[0]:
        return True
    return False


def send_email(sender, receiver, message):
    username = email_sender.username
    password = email_sender.password

    auto_email_sender = smtplib.SMTP("smtp.gmail.com:587")
    auto_email_sender.starttls()
    auto_email_sender.login(username, password)
    auto_email_sender.sendmail(sender, receiver, message)
    auto_email_sender.quit()


def send_forgotten_password_email(hash, username):
    sender = email_sender.email
    cursor.execute("SELECT email FROM clients WHERE username = ?", (username,))
    result = cursor.fetchone()
    receiver = result[0]

    message = """Hi, this is your new password -->{}<-- .
    We advise you to change it.""".format(hash)
    send_email(sender, receiver, message)


def send_otp_email(username, otps):
    sender = email_sender.email
    cursor.execute("SELECT email FROM clients WHERE username = ?", (username,))
    result = cursor.fetchone()
    receiver = result[0]
    message = "List of your one-time-usable banking passwords:\n"
    for count in range(0, number_of_otp-1):
        message += otps[count]+"\n"
    message += otps[number_of_otp-1]
    send_email(sender, receiver, message)


def send_reset_password(username):
    generated_hash = generate_random_hash()
    hashed_hash = hashlib.sha1(generated_hash.encode('utf-8')).hexdigest()
    cursor.execute("UPDATE clients SET password = ? WHERE username = ?", (hashed_hash, username))
    conn.commit()
    send_forgotten_password_email(generated_hash, username)


def otp_generator():
    return (binascii.b2a_hex(os.urandom(15))).decode("utf-8")


def get_otp_for_user(username):
    ID = get_user_id(username)
    cursor.execute("SELECT otp FROM otps WHERE id = ?", (ID,))
    result = cursor.fetchall()
    otp = []
    for row in result:
        otp.append(row[0])
    return otp


def remove_used_otp(username, otp):
    ID = get_user_id(username)
    cursor.execute("DELETE FROM otps WHERE id = ? AND otp = ?", (ID, otp))
    conn.commit()


def fill_otps_table_for_user(username, otp_key_list):
    ID = get_user_id(username)
    otp_tuple_list = []
    for item in otp_key_list:
        otp_tuple = (ID, item)
        otp_tuple_list.append(otp_tuple)
    cursor.executemany("INSERT INTO otps (id, otp) VALUES (?,?)", otp_tuple_list)
    conn.commit()


def get_otp(username):
    one_time_keys = get_otp_for_user(username)
    if one_time_keys != []:
        print ("You have {} unused keys.".format(len(one_time_keys)))
    elif one_time_keys == []:
        otps = []
        for count in range(0, number_of_otp):
            otps.append(otp_generator())
        send_otp_email(username, otps)
        fill_otps_table_for_user(username, otps)


def update_deposit(username, current_money):
    cursor.execute("UPDATE clients SET balance = ? WHERE username = ?", (current_money, username))
    conn.commit()
