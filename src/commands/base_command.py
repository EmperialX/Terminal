class BaseCommand:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def execute(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement this method.")

    def help(self):
        return f"{self.name}: {self.description}"