#Programmet takler diverse variabler og input, og bruker f-strings for enkel formatering

navn = input("Hva heter du? \n")

print(f"Hei {navn}!")

x = 3141
y = 2048

print(x)
print(y)

differanse = x - y

print(f"Differanse: {differanse}")

nyttNavn = input("Velg et annet navn. \n")

sammen = navn + nyttNavn

print(sammen)

sammen = f"{navn} og {nyttNavn}"

print(sammen)