import logging
import os

class Logger:
    def __init__(self, log_file='terminal.log'):
        self.logger = logging.getLogger('InteractiveTerminal')
        self.logger.setLevel(logging.DEBUG)
        
        # Create a file handler
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.DEBUG)
        
        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create a formatter and set it for both handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add the handlers to the logger
        self.logger.addHandler(handler)
        self.logger.addHandler(console_handler)

    def log_command(self, command):
        self.logger.info(f'Command executed: {command}')

    def log_error(self, error):
        self.logger.error(f'Error occurred: {error}')

    def log_message(self, message):
        self.logger.debug(message)

    def log_execution(self, command, result):
        self.logger.info(f'Command: {command} | Result: {result}')