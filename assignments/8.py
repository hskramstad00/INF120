# Assignment 8
# Lage klasser for ulike familiedyr. Lage klasser for katt, hund, undulat
# Hver klasse skal ha attributt for antall bein og for dyre slag
# Skal også ha en funksjon som lag_familiedyr, som tar imot antall som argument
import random

class Katt:
    def __init__(self):
        self.antall_bein = 4
        self.dyre_slag = "Katt"

    def __str__(self):
        return f'Dyret er en {self.dyre_slag} med {self.antall_bein} bein.'
    

class Hund:
    def __init__(self):
        self.antall_bein = 4
        self.dyre_slag = "Hund"

    def __str__(self):
        return f'Dyret er en {self.dyre_slag} med {self.antall_bein} bein.'
    
class Undulat:
    def __init__(self):
        self.antall_bein = 4
        self.dyre_slag = "Undulat"

    def __str__(self):
        return f'Dyret er en {self.dyre_slag} med {self.antall_bein} bein.'
    
def lag_familedyr(antall =2):
    katt = Katt()
    hund = Hund()
    undulat = Undulat()
    dyr_alle = [katt, hund, undulat]
    dyr_i_huset = []

    for i in range(antall):
        valgt_dyr = random.choice(dyr_alle)
        dyr_i_huset.append(valgt_dyr)

    return dyr_i_huset


print('Første del:')
d1 = Katt()
print(d1)

print("Andre del:")
familiedyr = lag_familedyr(4)

for i, dyr in enumerate(familiedyr):
    print(f'{i+1}: {dyr}')