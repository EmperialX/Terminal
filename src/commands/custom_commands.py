class CustomCommand(BaseCommand):
    def __init__(self, name, description, execute_function):
        super().__init__(name, description)
        self.execute_function = execute_function

    def execute(self, *args, **kwargs):
        return self.execute_function(*args, **kwargs)

def add_custom_command(name, description, execute_function):
    command = CustomCommand(name, description, execute_function)
    # Here you would typically register the command in the command processor
    return command

# Example usage
if __name__ == "__main__":
    def sample_command(*args):
        return f"Sample command executed with arguments: {args}"

    custom_cmd = add_custom_command("sample", "A sample custom command", sample_command)
    print(custom_cmd.execute("arg1", "arg2"))  # This line is for demonstration purposes only.