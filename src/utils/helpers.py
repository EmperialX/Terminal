def parse_command_line_args(args):
    # Function to parse command line arguments
    parsed_args = {}
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            parsed_args[key] = value
    return parsed_args

def format_output(output):
    # Function to format output for display
    return str(output).strip()

def validate_command(command):
    # Function to validate the command format
    if not command:
        raise ValueError("Command cannot be empty.")
    return command.strip()