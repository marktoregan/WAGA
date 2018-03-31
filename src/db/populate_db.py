from tinydb import TinyDB, Query

db = TinyDB('db.json')
db.insert({"evp": "a", "charge_type": "fast", "location": [0, 1], "charge_time_required": 25})
db.insert({"evp": "b", "charge_type": "fast", "location": [0, 2], "charge_time_required": 25})
db.insert({"evp": "c", "charge_type": "fast", "location": [0, 3], "charge_time_required": 25})
db.insert({"evp": "d", "charge_type": "fast", "location": [1, 0], "charge_time_required": 25})
db.insert({"evp": "e", "charge_type": "fast", "location": [2, 0], "charge_time_required": 25})
db.insert({"evp": "f", "charge_type": "fast", "location": [3, 0], "charge_time_required": 25})

