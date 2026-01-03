import pandas as pd

# Oppgaven skal lese inn data fra en tekstfil med Pandas og bruke Matplotlib til å plotte
# disse dataene. Dataen inneholder daglig tempratur fra 2012 i Ås

# Del 1
# Bruke Pandas read_csv til å lese inn dataen til en Pandas DataFrame

df = pd.read_csv('data/meteodata_aas_2012.csv', sep=';', header=1)

print('PART 1:')
print(f'{df} \n')

# Del 2
# Plotte tempraturdata med bare kolonen T_avg og konvertere til numpy array

import matplotlib.pyplot as plt

# selecting average temprature
temp_avg = df['T_avg']

print('PART 2:')

temp_avg_numpy = temp_avg.to_numpy()
plt.plot(temp_avg_numpy, label='Daily average meassurement')
plt.legend(loc='upper right')
plt.ylabel('Temp [deg C]')
plt.xlabel('day of year')
plt.title('Temprature readings for 2012')
plt.show()
print('\n')

# Part 3
# Lag en funksjon som beregner tempratur gjennom året med gitt formel
# Plot funksjonen sammen med målte tempraturer
print('PART 3:')
import math

def year_temp(days):
    T_avg = 10
    A = 20
    offset = 0
    omega = 2 * math.pi / 365

    return T_avg + A * math.sin(omega * (days + offset))