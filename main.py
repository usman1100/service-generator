import random

data = open("./data.txt")

nouns = [i.replace("\n", "") for i in data.readlines()]

service = random.choice(nouns).capitalize()

print(f"{service} As Service ({service[0]}aS)")