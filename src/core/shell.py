class Shell:
    def __init__(self, command_processor):
        self.command_processor = command_processor

    def run(self):
        while True:
            try:
                user_input = input(">>> ")
                if user_input.lower() in ["exit", "quit"]:
                    print("Exiting the interactive terminal.")
                    break
                self.process_command(user_input)
            except Exception as e:
                print(f"Error: {e}")

    def process_command(self, command):
        result = self.command_processor.process(command)
        if result is not None:
            print(result)