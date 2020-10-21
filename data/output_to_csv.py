import json
import re
import os
import pathlib

with open("output.json") as file:
    with open("output.csv", "w") as csv:
        islanders = json.loads(file.read())
        csv.write("cancer,non_smoker,light_smoker,moderate_smoker,heavy_smoker\n")
        for islander in islanders:
            non_smoker = str(int(islander["smoke_level"] == 0))
            light_smoker = str(int(islander["smoke_level"] == 1))
            moderate_smoker = str(int(islander["smoke_level"] == 2))
            heavy_smoker = str(int(islander["smoke_level"] == 3))
            csv.write(str(islander["cancer"]) + "," + non_smoker + "," + light_smoker + "," + moderate_smoker + "," + heavy_smoker + "\n")