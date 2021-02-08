# Textový Analyzátor
# Roman Matušek
#***********************#

# vstupní proměnné
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
UvitaciText = 'Dobrý den, vítejte v programu "Analyzátor textu."'
Oddelovac = '=+' * int(len(UvitaciText)/1.5)
Users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'} # slovnik dvojic "jmeno:heslo"

# Přivítání uživatele
print(" ", Oddelovac,
      UvitaciText.center(len(Oddelovac)),
      Oddelovac, " ", sep="\n"
)

# vstupy uživatele
UserName = input('Zadejte přihlašovací jméno: ')
Password = input('Zadejte své heslo: ')
UzivatelVstup = (UserName, Password) # vstupní údaje vložíme do TUPLE proměnné "Uživatel"

# kontrola registrovanách uživatelů - membership test
if UzivatelVstup not in Users.items():
      print('Vaše registrační údaje nejsou v pořádku.')
      print(Oddelovac, 'Konec programu. Nashledanou.', Oddelovac, sep="\n")
      quit()

print(Oddelovac,'Vyberte si jeden text, který se bude analyzovat.', sep="\n")
VyberTextu = int(input('Vyberte text pro analyzu. Vložte jedno z čísel z rozsahu 1-3.'))
print(Oddelovac, sep="\n")

# Analýza textu
if VyberTextu in {1,2,3}:
      SeznamSlov = TEXTS[VyberTextu-1].split()  #pomocny seznam pro procházení vybraného textu
      PocetSlov = 0
      PocetSlovVelkePismena = 0
      PocetSlovMalePismena = 0
      PocetSlovZacatekVelkePismeno = 0
      PocetCisel = 0
      SoucetCisel = 0
      DelkaSlova = list()
      CetnostDelek = dict()  #slovnik do které uložím jednotlivá slova s jejich délkou

      while SeznamSlov:
            Slovo = SeznamSlov.pop().strip(" ,./;: ")
            if Slovo.istitle():
                  PocetSlovZacatekVelkePismeno += 1
            elif Slovo.islower():
                  PocetSlovMalePismena += 1
            elif Slovo.isupper():
                  PocetSlovVelkePismena += 1
            elif Slovo.isdigit():
                  SoucetCisel += int(Slovo)
                  PocetCisel += 1
            PocetSlov += 1
            DelkaSlova.append(len(Slovo))  #plnění seznamu délkami jednotlivých

      while DelkaSlova: #procházení seznamu, hledání kolikrát se klíč opakuje
            PomSlovo = DelkaSlova.pop()
            CetnostDelek[PomSlovo] = CetnostDelek.get(PomSlovo, 0) + 1

      # vytvoření seznamu = sestupné setřídění podle párů slovníku
      CetnostDelekSeznam = sorted(CetnostDelek.items(), reverse = True)

      print(sep="\n")
      print(Oddelovac)
      print("Grafická analýza výskytu délky slov a jejich opakování")
      print(Oddelovac)

      while CetnostDelekSeznam:  # Výpis sloupcového grafu
            PomCetnost = CetnostDelekSeznam.pop()
            print(PomCetnost[0], '*' * PomCetnost[1], PomCetnost[1])

      #print(sep="\n")
      print(f"Ve vybraném textu je celkem {PocetSlov} slov.")
      print(f"Ve vybraném textu je celkem {PocetSlovVelkePismena} slov psaných velkými písmeny.")
      print(f"Ve vybraném textu je celkem {PocetSlovMalePismena} slov psaných malými písmeno.")
      print(f"Ve vybraném textu je celkem {PocetSlovZacatekVelkePismeno} slov začínající na velké písmeno.")
      print(f"Ve vybraném textu je celkem {PocetCisel} slov, které jsou číslice.", sep="\n\n")

      print(sep="\n")
      print(Oddelovac)
      print(f"Součet všech čísel obsažených ve vybraném textu je: {SoucetCisel}.")
      print (Oddelovac)

else:
      print('Vámi vybraný text je mimo rozsah!', sep="\n")
      print(Oddelovac, 'Konec programu. Nashledanou.', Oddelovac, sep="\n\n")
      quit()


