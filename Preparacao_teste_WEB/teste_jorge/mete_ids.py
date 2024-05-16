import json
import sys

def acrescenta_ids(nome_ficheiro):
    # Read data from JSON file
    with open(nome_ficheiro, 'r') as file:
        data = json.load(file)

    for i, item in enumerate(data):
        item['_id'] = str(i + 1)
  
    with open('nova_bd.json', 'w') as file:
        json.dump(data, file, indent=4)
    
acrescenta_ids(sys.argv[1])