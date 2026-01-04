# Assignment 6
# Skal lese gjennom norec_corpus.txt og telle hvor ofte antall bokstaver blir brukt
# Finnes også tegn som ikke skal telles
# Ønsker ikke å skille på store og små bokstaver

text = 'data/norec_corpus.txt'
decoding_text = open(text, 'r', encoding='utf-8')

letters = {}
# can also use sum(letters.value()), but since assignment specifies using a variabel to
# count number of letters
total_letters = 0
exclude_chars = [
    ' ', '\n', ',', '.', '-', '–', '—', '*', '(', ')',
    '«', '»', ':', ';', '’', '?', "'", '"', '/', '!', '…',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for line in decoding_text:
    line = line.strip()

    # convert all to upper
    line = line.upper()

    for chars in line:
        if chars not in exclude_chars:
            total_letters += 1
            if chars in letters:
                letters[chars] = letters[chars] + 1
            else:
                letters[chars] =1

# making the dicitonary with realtive frequency
relative_frequency = {keys: values / total_letters *100 for keys, values in letters.items()}

# changing from dict to tuples
tuples_list = list(relative_frequency.items())

def order_by(tup):
    return tup[1]

sorted_tuples = sorted(tuples_list, key=order_by, reverse=True)

print(f'Counted letters: {total_letters}')
for x,y in sorted_tuples:
    print(f'{x} {y:.2f}%')