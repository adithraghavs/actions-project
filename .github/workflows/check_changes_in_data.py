import json
data = open("data.xml").read()
history = json.loads(open("history.json", "r").read())
if history[list(history.keys())[-1]] != data:
    with open("main.txt", "w") as file:
        file.write(data.split('<color name="')[1].split('">Ipsum<color>')[0])