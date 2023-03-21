def actors_all(cursor):

    # Haetaan kaikki tiedot kaikista nimikkeistä
    query = ("SELECT * FROM actors;")
    cursor.execute(query)

    actors = cursor.fetchall()

    if actors:
        print("\nKaikki näyttelijät:\n")
        for actor in actors:
            print(str(actor['id'])+ ". " + actor['first_name'] + " " + actor['last_name'])
    else:
        print("\nEi näyttelijöitä.")
