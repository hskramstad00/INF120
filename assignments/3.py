# Assignment 3

# Et program for bestilling av varer
# Tar input fra bruker om hvilke varer de vil kjøpe
# og hvor mange av hver vare og regner ut total pris


# funksjon for innlesning av alle varene til brukeren og returnerer en liste
def innlesning():
    shopping_list = []
    while True:
        product_name = input('Vare beskrivelse (blank for å avslutte innlesning): ')
        if product_name == '':
            print('Ferdig med innstasting av varer. Skriver nå ut og kvittering')
            return shopping_list
    
        while True:
            try:
                number = float(input('Antall: '))
                break
            except ValueError:
                print('Antall må være tall')
            
        while True:
            try:
                price = float(input('Pris: '))
                break
            except ValueError:
                print('Pris må være tall')
            
        # save to list
        shopping_list.append((product_name, number, price))        


# funksjon for utskrift av kvitteringen
def utskrift():
    shopped = innlesning()
    print(f"{'Beskrivelse':<15}{'Linjekost':>10}")
    print('----------------------------------')
    totalt = 0
    for groceries in shopped:
        totalt += groceries[1] * groceries[2]
        print(f"{groceries[0]:<15}{groceries[1]*groceries[2]:>7.2f}{'kr':>3}")
    print('----------------------------------')
    print(f"{'Sum':<15}{totalt:>7.2f}{'kr':>3}")

utskrift()