import os

class TrophyManager:
    def __init__(self, filename="trophies.txt"):
        self.filename = filename
        self.trophies = self.load_trophies()

    def load_trophies(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    return int(f.read())
                except ValueError:
                    return 0
        return 0

    def save_trophies(self):
        with open(self.filename, 'w') as f:
            f.write(str(self.trophies))

    def add_trophies(self, amount):
        self.trophies += amount
        self.save_trophies()

    def get_trophies(self):
        return self.trophies
