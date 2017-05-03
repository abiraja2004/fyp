import json

with open('sampleinput.json' , 'r') as reader:
    jf = json.loads(reader.read())

print(jf['http://d.opencalais.com/genericHasher-1/08452ca7-7080-3785-ab68-70ea91275ed6'])
