#exercitii 2
bec = 'nedefinit'
retea = 'nedefinit'
intrerupator = 'nedefinit'
situatie = input(f'Aveti lumina in incapere? Scrieti cu "DA" sau "NU"')
bypass_intrerupator = False
voltaj_retea = 'nedefinit'
if situatie == "DA":
    intrerupator = 'pornit'
    voltaj_retea = '220'
    retea = 'functionala'
    bec = 'aprins'
    print(f'''Ati spus ca aveti lumina in incapere, rezulta ca:
     - reteaua este {retea}
     - voltajul in retea este {voltaj_retea}
     - intrerupatorul este {intrerupator}
     - becul nu este ars
''')
elif situatie != 'DA': # verificam daca reteaua este functionala si daca este curent la 220 volti
    retea = input('Aveti curent in retea? Raspundeti cu "DA" sau "NU"')
    if retea == 'DA': # verificam daca voltajul din retea este este cel necesar
        retea = 'functionala'
        voltaj_retea = input('Introduceti intensitatea curentululi in retea: ')
        if voltaj_retea == '220' and retea == 'functionala':  # daca reteaua este functionala si voltajul este cel necesar
            retea = 'conforma'
            print('Raport instalatie electrica:')
            retea = 'conforma'  # daca reteaua este conforma, verificam daca intreupatorul este pornit
            print(f'''            - reteaua este {retea}
            - voltajul este {voltaj_retea}
            - putem sa pornim in siguranta intrerupatorul''')
            intrerupator = input('Porniti intrerupatorul si raspundeti daca se aprinde becul! Raspundeti cu "DA" sau "NU"')
            if intrerupator == "DA":  # verificam daca intrerupatorul este pornit si becul nu este ars
                intrerupator = 'DA'
                bec = 'aprins'
            if bec == 'aprins':  # daca intrerupatorul este pornit si becul este aprins atunci raport
                print('Problema este rezolvata! A trebuit sa porniti intrerupatorul!')
            else:
                bec = 'ars'
                print(f'Becul este {bec}, schimbati becul!')
        else: print('Reteaua nu este conforma, aveti nevoie de 220 de volti pentru a functiona!')
        retea = 'neconforma'
    elif retea != 'DA':
        retea = 'nefunctionala'
        print(f'Trebuie sa aveti curent in retea, faceti o sesizare la enel, reteaua este {retea}!')




