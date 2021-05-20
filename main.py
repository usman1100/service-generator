import random

nouns = open("./nouns.txt")
adjectives = open("./adjectives.txt")

nouns = [i.replace("\n", "") for i in nouns.readlines()]
adjectives = [i.replace("\n", "") for i in adjectives.readlines()]

service = random.choice(nouns).capitalize()
quality = random.choice(adjectives).capitalize()

print(f"{quality} {service} As Service ({quality[0]}{service[0]}aS)")