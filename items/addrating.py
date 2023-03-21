def add_rating(cursor):

    query = ("SELECT id, name FROM titles;")
    cursor.execute(query)

    titles = cursor.fetchall()

    if titles:
        print("\nKaikki nimikkeet:")
        for title in titles:
            print(f"{title['id']}. {title['name']}")
    else:
        print("\nEi nimikkeitä.")

    id = input("\nMinkä nimikkeen haluat arvostella? (syötä numero)\n")
    user = input("Anna käyttäjätunnus (sähköpostiosoitteesi)\n")
    rate = input("Anna pistearvoiointi (1, 1.5, 2, 2.5, 3, 3.5 ,4 ,4.5 ,5)\n")

    # Lisätään arvostelu nimikkeelle.
    query = ("INSERT INTO ratings(titles_id, users_id, rating) "
             "VALUES("
             "(%s), "
             "(SELECT id FROM users WHERE users.email = (%s)), "
             "(%s))")
    cursor.execute(query, (id, user, rate))

    print("\nLisätään arvostelu valitsemaasi nimikkeeseen:")
    print(f"Käyttäjätunnus: {user}")
    print(f"Pisteet: {rate}")

