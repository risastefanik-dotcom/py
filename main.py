import sys
titlecase=0
uppercase=0
lowercase=0
pocet_cisel = 0
soucet_cisel = 0
cetnosti = {}
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
jmeno= input ("Zadej jméno: ")
heslo = input ("Zadej heslo: ")
if jmeno not in uzivatele:
    print ("Wrong name")
    sys.exit()
elif uzivatele[jmeno] != heslo:
    print ("Wrong password")
    sys.exit()
else:
    print(f"Welcome to the app, {jmeno}!")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    try:
        vyber = int(input("Enter a number btw. 1 and 3 to select: "))

        if vyber < 1 or vyber > len(TEXTS):
            print("Invalid number, exiting program.")
            sys.exit()
        else:
            text = TEXTS[vyber - 1]
            print(f"You selected text number {vyber}.")
            slova = text.split()
            pocet_slov = len(slova)
            for slovo in slova:
                cislo = slovo.strip(".,")
                if slovo.istitle():
                    titlecase += 1
                elif slovo.isupper():
                    uppercase += 1
                elif slovo.islower():
                    lowercase += 1
            print(f"There are {pocet_slov} words in the selected text.")
            print(f"There are {titlecase} title case words in the selected text.")
            print(f"There are {uppercase} upper case words in the selected text.")
            print(f"There are {lowercase} lower case words in the selected text.")
            for slovo in slova:
                cislo = slovo.strip(".,")
                if cislo.isdigit():
                    pocet_cisel += 1
                    soucet_cisel += int(cislo)
            print(f"There are {pocet_cisel} numeric strings in the selected text.")
            print(f"The sum of all the numbers {soucet_cisel}.")
            for slovo in slova:
                delka = len(slovo.strip(".,"))
                if delka not in cetnosti:
                    cetnosti[delka] = 1
                else:
                    cetnosti[delka] += 1
            serazene_cetnosti = sorted(cetnosti.items())
            print("-" * 40)
            print("LEN|  OCCURRENCES  |NR.")
            print("-" * 40)
            for delka, pocet in serazene_cetnosti:
                print(f"{delka:>3}|{'*' * pocet:<20}|{pocet}")
                
    except ValueError:
        print("Invalid input, exiting program.")
        sys.exit()