from random import randint

def roll(sides=6, dice=1):
    '''Rolls arbitrary number of n-sided dice), default 1d6.'''
    out = 0
    for d in range(dice):
        out += randint(1, sides)
    return out

def r4d20_itemized():
    '''Returns a list of four d20's rolled.'''
    out = []
    for d in range(4):
        out.append(roll(20))
    return out

def r2d6():
    return roll() + roll()

def families_make():
    '''Creates families.
    Roll sets of 4d20. Each d20 is a family. Stop (using entire set) when the
    total population meets or exceeds 100.'''
    families = {} 
    # families structure = family name : number of people in family
    
    while sum(families.values()) < 100:
        for people in r4d20_itemized():
            name = 'family' + str(len(families))
            families[name] = people
    
    return families

def sort_families_by_pop(families, low_first=False):
    '''Returns dict of families sorted by their population, largest to
    smallest by default.'''
    sorted_families = {}
    if not low_first:
        vals = reversed(sorted(families.values()))
    else:
        vals = sorted(families.values())

    for v in vals:
        for f in families:
            if families[f] == v:
                sorted_families[f] = v

    return sorted_families

def basic_stats(runs=2000):
    '''Tracks monte-carlo stats, 2000 runs by default.
    Average population of the village.
    Average number of families in the village.'''
    average_population = 0
    average_families = 0
    
    for r in range(runs):
        families = families_make()
        average_population += sum(families.values())
        average_families += len(families)

    average_population /= runs
    average_families /= runs

    print(f'Avg. Population: {average_population}')
    print(f'Avg. Number of Families: {average_families}')

def families_report_better():
    families = families_make()

    print(f'''Village Population: {sum(families.values())}
Number of families: {len(families)}\n\nFamilies:''')
    families = sort_families_by_pop(families)
    for f in families:
        print(f'{f}: {families[f]}')
    
def families_report():
    '''Prints the families and their number of members in the village, and the
    village's population.'''
    families = families_make()
    print(f'Families: {families}')
    print(f'Population: {sum(families.values())}')
    
if __name__ == '__main__':
    families_report_better()


# Avg. Population: 122.99
# Avg. Number of Families: 11.748
# When using fistfulls of 10d20, average pop only rose to 145. I bet
# this would be an interesting curve.
