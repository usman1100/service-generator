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

nouns = open("./nouns.txt")
adjectives = open("./adjectives.txt")

nouns = [i.replace("\n", "") for i in nouns.readlines()]
adjectives = [i.replace("\n", "") for i in adjectives.readlines()]

for i in range(times):
    service = random.choice(nouns).capitalize()
    quality = random.choice(adjectives).capitalize()

    print(f"{quality} {service} As Service ({quality[0]}{service[0]}aS)")