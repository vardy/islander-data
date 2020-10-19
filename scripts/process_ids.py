import json
import re

match_id = r"\"(.*)\""
ids = []

# For each line in IDs file, extract value from inside
# of first set of quotes found, append to `ids` array.
id_file = open("reading_ids.txt", "r")
lines = id_file.readlines()
for line in lines:
    matches = re.finditer(match_id, line, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        ids.append(match.group(1))
id_file.close()

# Remove duplicates
ids = list(set(ids))

# Write JSON array to file
with open("processed_ids.txt", "w") as output:
    json.dump(ids, output)
