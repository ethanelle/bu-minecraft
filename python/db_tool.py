from pathlib import Path
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
import boto3
import os
import re

regex_displayName = re.compile('\blastAccountName: ')
regex_lastLogin = re.compile('\blogin: ')
regex_lastLogout = re.compile('\blogout: ')

access_file = open(str(Path.home()) + "/.dynamodb_key", "r")
keys = access_file.read().split(':')
ACCESS_KEY = keys[0]
SECRET_KEY = (keys[1])[:len(keys[1])-1]
access_file.close()

client = boto3.resource('dynamodb',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name='us-east-2')

table = client.Table("bumc-players")

def update_entry(uid, displayName, lastLogin, lastLogout):
    try:
        response = table.update_item(
            Key={
                'playerId': uid
            },
            AttributeUpdates={
                'display name': displayName,
                'last login': lastLogin,
                'last logout': lastLogout,
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print('Success:\t' + item['display name'])

def save_file(uid, lines):
    displayName = ""
    lastLogin = ""
    lastLogout = ""

    for line in lines:
        if regex_displayName.match(line) != None:
            displayName = line[regex_displayName.match(line).end():]
        elif regex_lastLogin.match(line) != None:
            lastLogin = line[regex_lastLogin.match(line).end():]
        elif regex_lastLogout.match(line) != None:
            lastLogout = line[regex_lastLogout.match(line).end():]
        if not(displayName == "" or lastLogin == "" or lastLogout == ""):
            break
    
    update_entry(uid, displayName, lastLogin, lastLogout)

def init_db():
    path = str(Path.home()) + "/game_server/plugins/Essentials/userdata/"
    for file in os.listdir(path):
        if file.endswith('.csv'):
            f = open(file, "r")
            contents = f.read()
            f.close()
            save_file(file[:-3], contents.split('\n'))

init_db()