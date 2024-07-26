import json
import random
import uuid
deck = json.load(open("52-deck.json"))
random.shuffle(deck)
name = uuid.uuid4().hex;
json.dump(deck, open("%s.json" % name, "w"))
index = json.load(open("index.json"))
index.append(name)
json.dump(index, open("index.json", "w"))
