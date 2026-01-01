# Assignment 4

# Lager et script for å lese veridene for vekt og naturlig forekomst for oksygen sine isotoper.
# Beregn oksygens molare masse. Skriv resultatet med 4 desimalers presisjon og riktig måleenhet

total_molar_mass = 0

with open('data/Oxygen.txt','r') as oxygen_file:
    # skip header
    next(oxygen_file)

    for line in oxygen_file:
        Isotype, Weight, Natural_adbuance = line.strip().split()
        Weight = float(Weight)
        Natural_adbuance = float(Natural_adbuance)

        total_molar_mass += Weight * Natural_adbuance

    print(f'Total molar mass for oxygen is: {total_molar_mass:.4f} [g/mol]')
