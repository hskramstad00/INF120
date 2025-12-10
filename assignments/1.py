# First assignment 

# år, totalt innsamlet, antall bøssebærer
innsamling_hist = [
    [2015, 86343, 123],
    [2016, 93512, 125],
    [2017, 83935, 119],
    [2018, 91274, 128],
    [2019, 88935, 127],
    [2020, 95182, 132],
    ]

# Del 1
# Utskrift av insamlet beløp hvert år, og gj.snitt innsamlet pr bøssebærer
# Bruk streng formatering til å begrense antall desimaler for kronebeløpet til 2

for innsamled in innsamling_hist:
    print(f'{innsamled[0]}: {innsamled[1]/innsamled[2]:.2f} kr/bøssebærer')

# Del 2
# Hvilket år ble det samlet inn mest penger pr bøssebærer

max_innsamled = 0

for max in innsamling_hist:
    per_bøssebærer = max[1] / max[2]

    if per_bøssebærer > max_innsamled:
        max_innsamled = per_bøssebærer
        max_år = max[0]

print(f'Det ble samlet inn mest penger i år {max_år}')