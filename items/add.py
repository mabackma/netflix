def add(cursor):

    name = input("\nAnna nimi (pakollinen): ")
    year = input("Anna ilmestymisvuosi (pakollinen): ")
    running_time = input("Anna nimikkeen kesto (pakollinen): ")
    description = input("Anna kuvaus (vapaaehtoinen): ")
    age_rating = input("Anna suositusikäraja: ")

    # Haetaan media tyypit.
    query = "SELECT id, type FROM media_types;"
    cursor.execute(query, )
    media_types = cursor.fetchall()
    all_types = ""
    if media_types:
        for media_type in media_types:
            all_types += f"{media_type['type']}({media_type['id']})|"
        all_types = all_types[:-1]
        type = input(f"Anna nimikkeen tyyppi numerona (pakollinen, {all_types}): ")

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