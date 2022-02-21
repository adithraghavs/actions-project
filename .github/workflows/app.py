import json, subprocess

history = open("history.json", "r")
history_dict = json.loads(history.read())

data = open("data.xml").read()
hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode()[:-2]
history_dict[hash] = data
history_json = json.dumps(history_dict, indent=4)

history = open("history.json", "w+")
history.write(history_json)

history = open("history.json", "r")
print(history.read())

data = open("data.xml").read()
history = json.loads(open("history.json", "r").read())
if history[list(history.keys())[-1]] != data:
    print("hello")
    with open("main.txt", "w") as file:
        print("in with")
        file.write(data.split('<color name="')[1].split('">Ipsum<color>')[0])
        print("written file")