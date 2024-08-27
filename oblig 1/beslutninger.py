#Programmet lagrer svar fra brukeren som en variabel, og sjekker om det er ja, nei eller noe annet.

svar = input("Har du lyst på en brus? ja/nei \n")

if svar == "ja":
    print("Her har du en brus!")
elif svar == "nei":
    print("Den er grei.")
else:
    print("Det forsto jeg ikke helt.")