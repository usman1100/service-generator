import random
import sys

times = 0

if len(sys.argv) > 2:
    print("Usage: python3 main.py <n> OR python3 main.py")
    exit(1)

if len(sys.argv) == 2:
    times = int(sys.argv[1])
else:
    times = 1

nounsFile = open("./nouns.txt")
adjectivesFile = open("./adjectives.txt")

nouns = [i.replace("\n", "") for i in nounsFile.readlines()]
adjectives = [i.replace("\n", "") for i in adjectivesFile.readlines()]

nounsFile.close()
adjectivesFile.close()

for i in range(times):
    service = random.choice(nouns).capitalize()
    quality = random.choice(adjectives).capitalize()

    print(f"{quality} {service} As Service ({quality[0]}{service[0]}aS)")