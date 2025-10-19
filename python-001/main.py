
# globalVariables
prenom = input("Votre prénom : ") 
age = int(input("Votre age : "))

print(f"Bonjours {prenom}, vous avez {age} ans")
print(f"Dans 2 ans vous aurez {age + 2}")
r = True
while r:
    try:
        prenom = input("Votre prénom : ") 
        r = False
        
    except ValueError:
        print(f"Erreur, merci de recommencer")
