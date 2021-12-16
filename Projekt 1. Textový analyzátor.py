from typing import Text


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

#| USER |   PASSWORD  |
#-----------------------
#| bob  |     123     |
#| ann  |    pass123  |
#| mike | password123 |
#| liz  |    pass123  |

users = {"bob": "123",
 "ann": "pass123",
 "mike": "password123",
 "liz": "pass123"
 }

oddelovac = "=" * 70 

#--------------------------------------------------------------------------------------

uzivatel_jmeno = input("Zadej uživatelské jméno: ")

if uzivatel_jmeno not in users:
    print("Špatně zadané uživatelské jméno..  Ukončuji...")
    quit()
else:
    uzivatel_heslo = input("Zadej heslo: ")

if uzivatel_heslo != users.get(uzivatel_jmeno):
    print("Špatně zadané heslo.. Ukončuji...")
    quit()
else:
    print(oddelovac)
    print(f"Vítej v textovém analyzátoru, {uzivatel_jmeno}!")

print(oddelovac)
vyber_textu = input("Vyber si číslo textu, které chceš analyzovat - |1|2|3| - : ")
print(oddelovac)

if vyber_textu == "1":
    vybrany_text = TEXTS[0]
elif vyber_textu == "2":
    vybrany_text = TEXTS[1]
elif vyber_textu == "3":
    vybrany_text = TEXTS[2]
else:
    print("Špatně vybrané číslo textu! UKONČUJI...")
    quit()

#-------------------------------------------------------------------------------------------

vycisteni_text = []
pocet_slov = 0
slovo_title = 0
slovo_upper = 0
slovo_lower = 0
ciselne_stringy = 0
suma_cisel = 0
graf = {}

for slovo in vybrany_text.split():
    if len(slovo.strip(".:;,")) == 0:
        continue
    vycisteni_text.append(slovo.strip(".:;,").lower())
    pocet_slov = pocet_slov + 1
    if slovo.istitle() == True:
        slovo_title = slovo_title + 1
    elif slovo.isupper() == True:
        slovo_upper = slovo_upper + 1
    elif slovo.islower() == True:
        slovo_lower = slovo_lower + 1
    elif slovo.isnumeric() == True:
        ciselne_stringy = ciselne_stringy + 1
        suma_cisel = suma_cisel + int(slovo)

    
print(f"Ve vybraném textu se nachazí {pocet_slov} slov.")
print(f"Ve vybraném textu se nachazí {slovo_title} slov, které začínají velkým písmenem.")
print(f"Ve vybraném textu se nachazí {slovo_upper} slov, které jsou psaná velkými písmeny.")
print(f"Ve vybraném textu se nachazí {slovo_lower} slov, které jsou psaná malými písmeny.")
print(f"Ve vybraném textu se nachazí {ciselne_stringy} číselných stringů")
print(f"Suma všech čísel v textu je '{suma_cisel}'.")
print(oddelovac)
#-------------------------------------------------------------------------------------------------------

print("DÉLKA|  VÝSKYT  |POČET VÝSKYTU")
print(oddelovac)

for word in vycisteni_text:
    if len(word) in graf.keys():
        graf[len(word)] = graf[len(word)] + 1
    else:
        graf.update({len(word): 1})

serazeny_graf = dict(sorted(graf.items()))

for x,y in serazeny_graf.items():
    print(
    f"{x: >2}|{'*' * y: <15}|{y}",
    sep="\n")

print(oddelovac)