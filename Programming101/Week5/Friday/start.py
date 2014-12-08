import sql_manager
import os


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>").split(" ")

        if command[0] == 'register':
            username = input("Enter your username: ")
            os.system("stty -echo")
            password = input("Enter your password: ")
            os.system("stty echo")
            email = input("Enter your email address: ")

            print(sql_manager.register(username, password, email))

        elif command[0] == 'login':
            username = input("Enter your username: ")
            os.system("stty -echo")
            password = input("Enter your password: ")
            os.system("stty echo")

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command[0] == 'reset-password':
            if not sql_manager.check_if_username_exists(command[1]):
                print("Invalid username/password.")
            else:
                sql_manager.clear_login_attempts(command[1])
                sql_manager.send_reset_password(command[1])
                correct = False
                while correct is False:
                    probable_hash = input("Please enter the code you have received in the email: ")
                    if sql_manager.check_if_hashes_match(command[1], probable_hash):
                        correct = True
                sql_manager.login(command[1], probable_hash)
                os.system("stty -echo")
                new_password = input("Please enter your new password: ")
                os.system("stty echo")
                while sql_manager.check_password_strength(command[1], new_password) is False:
                    os.system("stty -echo")
                    new_password = input("Please enter a valid password: ")
                    os.system("stty echo")
                sql_manager.change_pass(new_password, command[1])

        elif command[0] == 'help':
            print("help - for displaying this message!")
            print("login - for logging in!")
            print("register - for creating new account!")
            print("reset-password <username> - for resetting forgotten password!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            os.system("stty -echo")
            new_pass = input("Enter your new password: ")
            os.system("stty echo")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'deposit':
            amount = float(input("Enter amount: "))
            otp_code = input("Enter OTP: ")
            available_otp = sql_manager.get_otp_for_user(logged_user.get_username())
            if otp_code in available_otp:
                logged_user.deposit(amount)
                sql_manager.remove_used_otp(logged_user.get_username(), otp_code)
                sql_manager.update_deposit(logged_user.get_username(), logged_user.get_balance())
                print("Deposit successful.")
            else:
                print("Deposit unsuccessful.")

        elif command == 'withdraw':
            amount = float(input("Enter amount: "))
            otp_code = input("Enter OTP: ")
            available_otp = sql_manager.get_otp_for_user(logged_user.get_username())
            if otp_code in available_otp:
                sql_manager.remove_used_otp(logged_user.get_username(), otp_code)
                result = logged_user.withdraw(amount)
                if result == "Withdraw successful.":
                    print (result)
                    sql_manager.update_deposit(logged_user.get_username(),
                                               logged_user.get_balance())
                else:
                    print("Withdraw unsuccessful.")
            else:
                print("Withdraw unsuccessful.")

        elif command == 'get-otp':
            sql_manager.get_otp(logged_user.get_username())

        elif command == 'help':
            print("help - for showing this message")
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    sql_manager.create_credentials_table()
    sql_manager.create_otp_table()
    main_menu()

if __name__ == '__main__':
    main()
