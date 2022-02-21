import json
history = open("history.json")
history_dict = json.loads(history.read())

data = open("data.xml").read()