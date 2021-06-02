def hra ():
#definice promennych
    oddelovac = '='*40
    znaky = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
    vypinac = 1
    pocitadlo = 0
#uvodni text
    print('Hra piskvorky zacina...')
    print(oddelovac)
    print('Kazde kolo muzes umistit svuj znak na\n'
          'jedno policko hraciho pole. Vyhrava ten,\n'
          'kdo spoji tri sve znaky. Znaky muzes\n'
          'spojit horizontalne, vertikalne i po\n'
          'diagonale.')
    print(oddelovac)
    print(('Pojdme zacit').center(40))
    print(oddelovac)
#start hry
    while vypinac:
        #vetev pro hrace o
        if pocitadlo % 2 == 0:
            print(oddelovac)
            tah = input('Hrac o | Prosim zadej cislo tahu:')
            print(oddelovac)
            #odfiltrovani spatne zadane odpovedi ve forme textu
            if not tah.isnumeric():
                print('Spatne zadany tah, hraj znovu:')
                continue
            #propsani mozne odpovedi
            elif int(tah) in range(1,10) and znaky[int(tah)-1]==' ':
                znaky[int(tah)-1] = 'o'
                pocitadlo = 1
                obrazec(znaky)
                vypinac = kontrola_cile(znaky)
                continue
            #spatna odpoved pokud je pole uz vybrane
            else:
                print('Spatne zadany tah, hraj znovu:')
                continue
        #vetev pro hrace x
        if pocitadlo % 2 == 1:
            print(oddelovac)
            tah = input('Hrac x | Prosim zadej cislo tahu:')
            print(oddelovac)
            #odfiltrovani spatne zadane odpovedi ve forme textu
            if not tah.isnumeric():
                print('Spatne zadany tah, hraj znovu:')
                continue
            #propsani mozne odpovedi
            elif int(tah) in range(1,10) and znaky[int(tah)-1]==' ':
                znaky[int(tah)-1] = 'x'
                pocitadlo = 0
                obrazec(znaky)
                vypinac = kontrola_cile(znaky)
                continue
            #spatna odpoved pokud je pole uz vybrane
            else:
                print('Spatne zadany tah, hraj znovu:')
                continue
#vizualizace obrazce
def obrazec (list_znaku):
    print(f"+---+---+---+".center(40))
    print(f"| {list_znaku[0]} | {list_znaku[1]} | {list_znaku[2]} |".center(40))
    print(f"+---+---+---+".center(40))
    print(f"| {list_znaku[3]} | {list_znaku[4]} | {list_znaku[5]} |".center(40))
    print(f"+---+---+---+".center(40))
    print(f"| {list_znaku[6]} | {list_znaku[7]} | {list_znaku[8]} |".center(40))
    print(f"+---+---+---+".center(40))
#kontrola, zda nebyla splnena podminka vyhry, pripadne zda nejsou vybrana vsechna pole
def kontrola_cile (znaky):
    if not znaky[0]== ' ' and znaky[0] == znaky [3] and znaky[3] == znaky[6]:
        print('Hrac',znaky[0],'vyhral, konec hry!')
        vypinac = 0
        return vypinac
    elif not znaky[1] ==' ' and znaky[1] == znaky [4] and znaky[4] == znaky[7]:
        print('Hrac',znaky[1],'vyhral, konec hry!')
        vypinac = 0
        return vypinac
    elif not znaky[2] ==' ' and znaky[2] == znaky [5] and znaky[5] == znaky[8]:
        print('Hrac',znaky[2],'vyhral, konec hry!')
        vypinac = 0
        return vypinac
    elif not znaky[0] ==' ' and znaky[0] == znaky [1] and znaky[1] == znaky[2]:
        print('Hrac',znaky[0],'vyhral, konec hry!')
        vypinac = 0
        return vypinac
    elif not znaky[3] ==' ' and znaky[3] == znaky [4] and znaky[4] == znaky[5]:
        print('Hrac',znaky[3],'vyhral, konec hry!')
        vypinac = 0
        return vypinac
    elif not znaky[6] ==' ' and znaky[6] == znaky [7] and znaky[7] == znaky[8]:
        print('Hrac',znaky[6],'vyhral, konec hry!')
        vypinac = 6
        return vypinac
    elif not znaky[0] ==' ' and znaky[0] == znaky [4] and znaky[4] == znaky[8]:
        print('Hrac',znaky[0],'vyhral, konec hry!')
        vypinac = 0
        return vypinac
    elif not znaky[2] ==' ' and znaky[2] == znaky [4] and znaky[4] == znaky[6]:
        print('Hrac',znaky[2],'vyhral, konec hry!')
        vypinac = 0
        return vypinac
    elif ' ' not in znaky:
        print('Vybrana vsechna pole, nikdo nevyhrava...')
        vypinac = 0
        return vypinac
    else:
        vypinac = 1
        return vypinac


hra()






