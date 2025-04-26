# Configuration settings for the interactive terminal application

# Default command settings
DEFAULT_COMMAND = "help"
DEFAULT_LOG_LEVEL = "INFO"

# Logging settings
LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOGGING_DATEFMT = "%Y-%m-%d %H:%M:%S"

# Command timeout settings
COMMAND_TIMEOUT = 5  # seconds

# Custom command settings
ENABLE_CUSTOM_COMMANDS = True

# System command settings
SYSTEM_COMMANDS = [
    "ls",
    "pwd",
    "cd",
    "exit"
]