import json, subprocess

history = open("history.json", "r")
history_dict = json.loads(history.read())

data = open("data.xml").read()
hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode()[:-2]
history_dict[hash] = data
history_json = json.dumps(history_dict, indent=4)

history = open("history.json", "w")
history.write(history_json)