import sys
import unittest

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '12asER>?_')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        result = sql_manager.register('Dinko', '1Dinko2')
        self.assertEqual(result, "Please enter a valid password.")

    def test_register_correct_data(self):
        result = sql_manager.register('Dinko', '12asER>?_')
        self.assertEqual(result, "Registration successful.")

    def test_login(self):
        logged_user = sql_manager.login('Tester', '12asER>?_')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_sql_injection_safety(self):
        logged_user = sql_manager.login("Tester", "' OR 1 = 1 --")
        self.assertFalse(logged_user)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '12asER>?_')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password_valid(self):
        logged_user = sql_manager.login('Tester', '12asER>?_')
        new_password = "45tyGH()%"
        result = sql_manager.change_pass(new_password, logged_user)
        self.assertEqual(result, "Password updated.")

    def test_change_password_invalid(self):
        logged_user = sql_manager.login('Tester', '12asER>?_')
        new_password = "123"
        result = sql_manager.change_pass(new_password, logged_user)
        self.assertEqual(result, "Please enter a valid password.")


if __name__ == '__main__':
    unittest.main()
