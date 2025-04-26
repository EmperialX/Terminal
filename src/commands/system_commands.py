class SystemCommand(BaseCommand):
    def execute(self, command):
        if command == "ls":
            return self.list_directory()
        elif command == "pwd":
            return self.print_working_directory()
        else:
            return "Command not found."

    def list_directory(self):
        import os
        return "\n".join(os.listdir('.'))

    def print_working_directory(self):
        import os
        return os.getcwd()