print("Dagens meny \n\nHovedretter: \n- Biff \n- Kylling \n- Falafel \n\nTilbehør: \n- Asparges \n- Fløtesaus \n")

hovedrett = input("Hvilken hovedrett vil du ha? \n")
tilbehør = input("Hvilket tilbehør vil du ha? \n")

if hovedrett == "Biff":
    if tilbehør == "Fløtesaus":
        print("Du spiser ikke nok grønnsaker!")
elif hovedrett == "Kylling":
    if tilbehør == "Fløtesaus":
        print("Du spiser ikke nok grønnsaker!")
elif hovedrett == "Falafel":
    if tilbehør == "Asparges":
        print("Du har valgt et vegetarmåltid")
else:
    print(f"Du har valgt {hovedrett} med {tilbehør}")
