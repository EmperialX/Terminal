import unittest
from src.core.terminal import Terminal
from src.core.command_processor import CommandProcessor

class TestTerminal(unittest.TestCase):

    def setUp(self):
        self.terminal = Terminal()
        self.command_processor = CommandProcessor()

    def test_initialization(self):
        self.assertIsNotNone(self.terminal)
        self.assertIsNotNone(self.command_processor)

    def test_command_prompt(self):
        prompt = self.terminal.get_prompt()
        self.assertEqual(prompt, ">>> ")

    def test_process_command(self):
        command = "echo Hello, World!"
        result = self.command_processor.process(command)
        self.assertIn("Hello, World!", result)

    def test_invalid_command(self):
        command = "invalid_command"
        result = self.command_processor.process(command)
        self.assertEqual(result, "Command not found.")

    def test_exit_command(self):
        command = "exit"
        result = self.command_processor.process(command)
        self.assertEqual(result, "Exiting terminal.")

if __name__ == '__main__':
    unittest.main()