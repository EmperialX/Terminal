# Usage Instructions for Interactive Terminal

## Overview

The Interactive Terminal is a powerful command-line interface that allows users to execute various commands directly from the terminal. This document provides guidance on how to use the terminal effectively, including command examples and usage instructions.

## Getting Started

To start the interactive terminal, run the following command in your terminal:

```
python main.py
```

Once the terminal is running, you will see a command prompt where you can enter commands.

## Basic Commands

### System Commands

The terminal supports several built-in system commands. Here are a few examples:

- **ls**: Lists the files and directories in the current working directory.
  ```
  ls
  ```

- **pwd**: Displays the current working directory.
  ```
  pwd
  ```

### Custom Commands

Users can also create and execute custom commands. To define a custom command, follow the syntax below:

```
create_command <command_name> <command_function>
```

For example, to create a command that prints "Hello, World!", you would use:

```
create_command hello_command print_hello
```

### Help Command

To get help on available commands, you can use the help command:

```
help
```

This will display a list of all available commands along with their descriptions.

## Command Execution

After entering a command, press `Enter` to execute it. The terminal will process the command and display the output or any error messages.

## Exiting the Terminal

To exit the interactive terminal, simply type:

```
exit
```

This will terminate the session and close the terminal window.

## Conclusion

The Interactive Terminal is designed to be user-friendly and extensible. Explore the available commands and customize your experience by creating your own commands. For further assistance, refer to the help command or consult the development documentation.