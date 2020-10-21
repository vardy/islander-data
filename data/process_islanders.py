import json
import re
import os
import pathlib

this_dir = pathlib.Path(__file__).parent.absolute()

match_id = r" id = '(.*?)';"
match_name = r"<title>(.*)</title>"
match_event = r"<tr><td>(\d*)/(\d*)</td><td>(.*)</td></tr>"

data = []
for filename in os.listdir(os.path.join(this_dir, "islanders")):

    cancer = 0
    smoke_level = 0
    id = -1
    name = ""

    with open(os.path.join(this_dir, "islanders", filename)) as file:
        html = file.read()

        # id
        matches = re.finditer(match_id, html, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            id = match.group(1)

        # name
        matches = re.finditer(match_name, html, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            name = match.group(1)

    with open(os.path.join(this_dir, "islanders", filename)) as file:
        for line in file.readlines():
            matches = re.finditer(match_event, line, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                text = match.group(3)
                if ("cancer" in text) and "Recovered" not in text:
                    cancer = 1
                if ("Light smoker" in text) and (smoke_level < 1):
                    smoke_level = 1
                if ("Moderate smoker" in text) and (smoke_level < 2):
                    smoke_level = 2
                if ("Heavy smoker" in text) and (smoke_level < 3):
                    smoke_level = 3
                break

    data.append({"name": name, "id": id, "cancer": cancer, "smoke_level": smoke_level})

with open(os.path.join(this_dir, "output.json"), "w") as out:
    out.write(json.dumps(data, indent=4))