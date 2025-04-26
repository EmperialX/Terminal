class CommandProcessor:
    def __init__(self, shell):
        self.shell = shell

    def process_command(self, command):
        command = command.strip()
        if not command:
            return "No command entered."

        # Split command into parts
        parts = command.split()
        command_name = parts[0]
        args = parts[1:]

        # Validate command
        if not self.validate_command(command_name):
            return f"Unknown command: {command_name}"

        # Delegate execution to the appropriate command handler
        return self.execute_command(command_name, args)

    def validate_command(self, command_name):
        # Here you can implement logic to check if the command is valid
        # For example, check against a list of known commands
        return command_name in self.shell.get_available_commands()

    def execute_command(self, command_name, args):
        # Here you would implement the logic to execute the command
        # This could involve calling the appropriate command class
        command_handler = self.shell.get_command_handler(command_name)
        if command_handler:
            return command_handler.execute(args)
        return "Command execution failed."