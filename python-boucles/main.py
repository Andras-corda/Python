Demander une valeur entière strictement positive
import random 
while True :

    try :
        N = int(input (f"Entrez une valeur entière strictement positive : "))
        if N > 0 :
            break
        else :
            print(f"Vous devez entrer une valeur positive ")
    except ValueError :
        print("Vous devez entrer une valeur numérique entière.")
alea = random.randint (1, N)
print(Alea)
essai = 0
while essai < 5 :
    essai += 1

    while True :
        try :
            nbre = int(input(f"{essai} - Valeur entre 1 et {N} : "))
            if nbre >= 1 and nbre <= N :
                break
            else :
                print(f"Vous devez entrer une valeur positive ")
        except ValueError :
            print("Vous devez entrer une valeur numérique entière.")
    if nbre == alea :
        print(f"Bravo ! Vous avez trouvé en {essai} coup(s)")
        break
    elif essai == 5 :
        print(f"Perdu ! Il fallait trouver {alea}")
    elif nbre < alea :
        print("Plus grand !")
    else :
        print("Plus petit !")