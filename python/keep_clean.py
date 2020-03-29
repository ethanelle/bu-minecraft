import os
from pathlib import Path

backups = []
path = str(Path.home()) + "/game_server/backups/"

for file in os.listdir(path):
    if file.endswith('.tar.gz'):
        backups.append(file)

if len(backups) > 8:
    backups.sort()
    file = backups[0]
    os.remove(path + backups[0])