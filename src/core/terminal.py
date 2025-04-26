class Terminal:
    def __init__(self):
        self.prompt = "> "
    
    def run(self):
        while True:
            try:
                command = input(self.prompt)
                if command.lower() in ['exit', 'quit']:
                    print("Exiting the terminal.")
                    break
                self.process_command(command)
            except KeyboardInterrupt:
                print("\nExiting the terminal.")
                break
            except Exception as e:
                print(f"Error: {e}")

    def process_command(self, command):
        # Placeholder for command processing logic
        print(f"Executing command: {command}")