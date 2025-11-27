import json

try:
    with open('modern_moves.json', 'r') as f:
        MOVES_DB = json.load(f)
except FileNotFoundError:
    print("Error: JSON files not found! Run 'modern_scraper.py' first.")
    MOVES_DB = {}

class Move:
    def __init__(self, name):

        if name not in MOVES_DB and not None and not "None":
            print(f"Warning: Move '{name}' not found in database.")
            name = "None"

        if name == "None" or name is None:
            self.name = "None"
            self.pwr = 0
            self.acc = 0
            self.pp = 0
            self.category = "Status"
            self.type = "Normal"
            self.prio = 0
            self.stat = {}
            self.status = "None"
            self.target = "normal"
            self.flags = {}
            return
        
        base = MOVES_DB[name]
        self.name = name
        self.pwr = base[0]
        self.acc = base[1]
        self.pp = base[2]
        self.category = base[3]
        self.type = base[4]
        self.prio = base[5]
        self.stat = base[6]
        self.status = base[7]
        self.target = base[8]
        self.flags = base[9]
