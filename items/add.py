def add(cursor):

    name = input("Anna nimi (pakollinen): ")
    year = input("Anna ilmestymisvuosi (pakollinen): ")
    running_time = input("Anna nimikkeen kesto (pakollinen): ")
    description = input("Anna kuvaus (vapaaehtoinen): ")
    age_rating = input("Anna suositusikäraja: ")
    type = input("Anna nimikkeen tyyppi numerona (pakollinen, leffa(1)|äänikirja(2)|peli(3)): ")

    # Lisätään nimike tietokantaan.
    query = ("INSERT INTO titles(name, year, running_time, description, age_rating, media_types_id) "
             "VALUES((%s), (%s), (%s), (%s), (%s), (%s))")
    cursor.execute(query, (name, year, running_time, description, age_rating, type))

    print("\nLisätään nimike:")
    print(f"Nimike: {name}")
    print(f"Ilmestymisvuosi: {year}")
    print(f"Kesto: {running_time}")
    print(f"Kuvaus: {description}")
    print(f"Suositusikäraja: {age_rating}")
    print(f"Tyyppi: {type}")