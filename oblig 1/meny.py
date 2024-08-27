print("Dagens meny \n\nHovedretter: \n- Biff \n- Kylling \n- Falafel \n\nTilbehør: \n- Asparges \n- Fløtesaus \n")

hovedrett = input("Hvilken hovedrett vil du ha? \n")
tilbehør = input("Hvilket tilbehør vil du ha? \n")

if hovedrett == "Falafel" and tilbehør == "Asparges":
    print("Du har valgt et vegetarmåltid")
elif hovedrett != "Falafel" and tilbehør == "Fløtesaus":
        print("Du spiser ikke nok grønnsaker!")
else:
    print(f"Du har valgt {hovedrett} med {tilbehør}")