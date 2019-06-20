import json
import os
test_method = 'hi i new module'


print(__package__)

print(os.getcwd())
with open('module/spam/config.json', 'r') as file:
    test2 = json.load(file)

print(test2)