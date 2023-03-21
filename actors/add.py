def add(cursor):

    first_name = input("Anna etunimi (pakollinen): ")
    last_name = input("Anna sukunimi (pakollinen): ")
    birth_date = input("Anna syntymäpäivä muodossa YYYY-MM-DD (pakollinen): ")

    # Lisätään näyttelijä tietokantaan.
    query = ("INSERT INTO actors(first_name, last_name, birth_date) "
             "VALUES((%s), (%s), (%s))")
    cursor.execute(query, (first_name, last_name, birth_date))

    print("\nLisätään näyttelijä:")
    print(f"Etunimi: {first_name}")
    print(f"Sukunimi: {last_name}")
    print(f"Syntymäpäivä (YYYY-MM-DD): {birth_date}")