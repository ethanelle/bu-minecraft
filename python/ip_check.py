from pathlib import Path
import os
import re

regex_ip = re.compile('ipAddress: \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
regex_name = re.compile('lastAccountName: .+')

path = str(Path.home()) + "/game_server/plugins/Essentials/userdata/"

matches = []

for file in os.listdir(path):
    if file.endswith('.yml'):
        f = open(path + str(file), "r")
        contents = f.read()
        f.close()
        match = re.search(regex_ip, contents)
        if match:
            ip = match.group(0).split(' ')[1]
            match = re.search(regex_name, contents)
            if match:
                name = match.group(0).split(' ')[1]
                pair = (name, ip)
                matches.append(pair)
            else:
                print('Error: found IP but no name in ' + str(file))

duplicates = []
while len(matches) > 0:
    names = []
    ip = ""
    for a,b in matches:
        if len(names) == 0:
            names.append(a)
            ip = b
            matches.remove((a,b))
        elif ip == b:
            names.append(a)
            matches.remove((a,b))
    if len(names) > 1:
        duplicates.append((ip, names))

print("Duplicates: ")
for dupe in duplicates:
    print(dupe)