# Assignment 6
# Skal lese gjennom norec_corpus.txt og telle hvor ofte antall bokstaver blir brukt
# Finnes også tegn som ikke skal telles
# Ønsker ikke å skille på store og små bokstaver

text = 'data/norec_corpus.txt'
decoding_text = open(text, 'r', encoding='utf-8')

letters = {}
exclude_chars = [
    ' ', '\n', ',', '.', '-', '–', '—', '*', '(', ')',
    '«', '»', ':', ';', '’', '?', "'", '"', '/', '!', '…',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for line in decoding_text:
    line = line.strip()

    # convert all to lower
    line = line.lower()

    for chars in line:
        if chars not in exclude_chars:
            if chars in letters:
                letters[chars] = letters[chars] + 1
            else:
                letters[chars] =1

for key in list(letters.keys()):
    print(key, " ", letters[key])