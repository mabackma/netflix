from actors.all import actors_all


def by_id(cursor):

    actors_all(cursor)

    id = input("\nAnna näyttelijän id: ")

    actor_details(cursor, id)


def actor_details(cursor, id):

    # Haetaan kaikki nimikkeen tiedot id:n perusteella.
    query = ("SELECT * FROM actors WHERE actors.id = (%s);")
    cursor.execute(query, (id,))

    actor = cursor.fetchone()
    if actor:
        print(f"\n{actor['first_name']} {actor['last_name']} {actor['birth_date']}")
    else:
        print("\nEi näyttelijää.")