
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''', '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''', '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']
oddelovac = '='*50
users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
slova_ocistene = []
pocet_slov = int()
pocet_slov_s_velkym_pismenem = int()
pocet_velkych_slov = int()
pocet_malych_slov = int()
pocet_cisel = int()
suma = int()
delka_slova = int()
slovnik_slov = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
                8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
                15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, }

'#pozdraveni uzivatele'

jmeno = input('Zadejte prosim sve prihlasovaci jmeno:')
heslo = input('Zadejte prosim sve heslo:')
print(oddelovac)

'#kontrola jmena a hesla'

if jmeno in users and heslo == users[jmeno]:
    print(f"Ahoj {jmeno}, vitam te v analyzatoru textu\n{oddelovac}")
else:
    print(f"Zadane jmeno nebo heslo neni v databazi registrovanych uzivatelu. Ukoncuji program...\n{oddelovac}")
    quit()

'#vyber textu'

vyber = int(input('Vyber prosim jeden ze tri textu.\n(1 = prvni text, 2 = druhy text, 3 = treti text)\nTvuj vyber:'))
if vyber not in [1, 2, 3]:
    print(f'{oddelovac}\nZadany vyber neodpovida zadnemu textu. Ukoncuji program...')
    quit()

'#ocisteni slov'

slova_neocistene = TEXTS[vyber-1].split(' ')
for x in slova_neocistene:
    x_ocistene = x.strip('.,')
    x_ocistene = x_ocistene.strip('\n')
    slova_ocistene.append(x_ocistene)
if '' in slova_ocistene:
    slova_ocistene.remove('')

'#pocitni slov'

for y in slova_ocistene:
    if y.isalpha() and y.istitle():
        pocet_slov_s_velkym_pismenem += 1
        pocet_slov += 1
    elif y.isalpha() and y.isupper():
        pocet_velkych_slov += 1
        pocet_slov += 1
    elif y.isalpha() and y.islower():
        pocet_malych_slov += 1
        pocet_slov += 1
    elif y.isdigit():
        pocet_cisel += 1
        suma += int(y)
        pocet_slov += 1
    elif y.istitle():
        pocet_slov_s_velkym_pismenem += 1
        pocet_slov += 1

'#pocitani delky slov'

for z in slova_ocistene:
    delka_slova = len(z)
    slovnik_slov[delka_slova] += 1

print(f'{oddelovac}', f'Pocet slov: {pocet_slov}',
      f'Pocet slov s velkym prvnim pismenem: {pocet_slov_s_velkym_pismenem}',
      f'Pocet slov s velkyma pismenama: {pocet_velkych_slov}',
      f'Pocet slov s malyma pismenama: {pocet_malych_slov}',
      f'Pocet cisel: {pocet_cisel}', sep='\n')
for x in slovnik_slov:
    if x < 10 and slovnik_slov[x] != 0:
        print(' ', x, '|', slovnik_slov[x]*'*', (20-slovnik_slov[x])*' ', '|', slovnik_slov[x])
    elif slovnik_slov[x] != 0:
        print('', x, '|', slovnik_slov[x]*'*', (20-slovnik_slov[x])*' ', '|', slovnik_slov[x])
    else:
        continue
