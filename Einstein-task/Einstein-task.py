import itertools
from pprint import pprint

def imright(h1, h2):
    return h1 - h2 == 1

def neighbours(h1, h2):
    return abs(h1 - h2) == 1

def zebra_puzzle():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next([Norwegian, Englishman, German, Swede, Dane, FISH]
        for (red, yellow, green, white, blue) in orderings
        if imright(white, green)        # белый дом находится справа от зелёного
        for (Norwegian, Englishman, German, Swede, Dane) in orderings
        if Norwegian is first           # норвежец живёт в первом доме
        if Englishman is red            # англичанин живёт в красном доме
        if neighbours(Norwegian, blue)  # норвежец живёт рядом с синим домом
        for (tea, milk, water, beer, coffee) in orderings
        if Dane is tea                  # датчанин пьёт чай
        if milk is middle               # живущий в центре пьёт молоко
        if green is coffee              # живущий в зелёном доме пьёт кофе
        for (Marlboro, Dunhill, PallMall, Winfield, Rothmans) in orderings
        if neighbours(Marlboro, water)  # курящий Marlboro и пьющий воду соседи
        if Dunhill is yellow            # курящий Dunhill живёт в жёлтом доме
        if German is Rothmans           # немец курит Rothmans
        if beer is Winfield             # курящий Winfield пьёт пиво
        for (cat, bird, dog, horse, FISH) in orderings
        if neighbours(Marlboro, cat)    # курящий Marlboro и выращивающий кошек соседи
        if bird is PallMall             # курящи PallMall выращивает птиц
        if Swede is dog                 # швед выращивает собак
        if horse is blue)               # живущий в синем доме выращивает лошадей

solution = zebra_puzzle()
nations = ["Norwegian", "Englishman", "German", "Swede", "Dane"]
d = dict(zip(solution[:-1], nations))

pprint(['%s live in house %s' % (d[i], i) for i in range(1, len(d) + 1)])

print ("\nOwner of the fish:", d[solution[-1]])
