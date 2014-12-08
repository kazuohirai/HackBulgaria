class CommandParser:
    def __init__(self, command_list):
        self.command_list = command_list

    def add_command(self, command, function):
        self.commands[command] = function

    def parse_command(self, command):
        if command in self.commands:
            return self.commands[command]
        else:
            return "Invalid command."
