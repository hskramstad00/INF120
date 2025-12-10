# Andre oppgave

# Inneholder fornavn og etternav
nameDB = [
     ['Tore', 'Hansen'],
     ['Silje', 'Olavsen'],
     ['Aase', 'Lund'],
     ['Jens Petter', 'Oremo'],
     ['Tina', 'Kittelsen'],
     ['Dag', 'Paulsen'],
     ['Lena', 'Nilsen'],
     ['Karsten', 'Woll'],
     ['Ine', 'Ørstad'],
     ['Ravn', 'Havnås'],
     ['Jesper', 'Danberg']]

# lage en funksjon som skal returnere True hvis noen kriteriere er oppfylt
# 1) fornavn begynner med T, 
# 2) etternavn har flere enn 6 tegn,
# 3) eller navn er Ravn Havnås

def name_check(fornavn, etternavn):
    if fornavn[0] == 'T':
        return True
    
    elif len(etternavn) > 6:
        return True
    
    elif fornavn == 'Ravn' and etternavn == 'Havnås':
        return True
    
    else:
        return False
    
# skrive ut personens navn hvis funksjonen retunerer True
# også skrive ut nummer is name_DB lista
# må plusse på 1 fordi index tar første i lista som 0
for index, name in enumerate(nameDB):
    check = name_check(name[0], name[1])
    if check == True:
        print(index+1,name[0], name[1])