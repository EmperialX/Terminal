import unittest
from src.commands.system_commands import LsCommand, PwdCommand
from src.commands.custom_commands import CustomCommand

class TestCommands(unittest.TestCase):

    def test_ls_command(self):
        command = LsCommand()
        output = command.execute()
        self.assertIsInstance(output, str)  # Check if output is a string
        self.assertIn("file1.txt", output)  # Check if a known file is in the output

    def test_pwd_command(self):
        command = PwdCommand()
        output = command.execute()
        self.assertIsInstance(output, str)  # Check if output is a string
        self.assertEqual(output, "/current/directory")  # Replace with expected current directory

    def test_custom_command_execution(self):
        custom_command = CustomCommand("echo Hello World")
        output = custom_command.execute()
        self.assertEqual(output.strip(), "Hello World")  # Check if the output matches the expected result

if __name__ == '__main__':
    unittest.main()