import json
import random
import uuid
deck = json.load(open("52-deck.json"))
random.shuffle(deck)
name = uuid.uuid4().hex;
json.dump(deck, open("%s.json" % name, "w"))
f = open("sets", "a")
f.write(name + "\n")
f.close()
