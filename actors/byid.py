from actors.all import actors_all


def by_id(cursor):

    actors_all(cursor)

    id = input("\nAnna näyttelijän id, jonka tiedot haluat nähdä: ")

    actor_details(cursor, id)


def actor_details(cursor, id):

    # Haetaan kaikki tiedot näyttelijästä id:n perusteella.
    query = ("SELECT * FROM actors WHERE actors.id = (%s);")
    cursor.execute(query, (id,))

    actor = cursor.fetchone()
    if actor:
        print(f"\n{actor['first_name']} {actor['last_name']} {actor['birth_date']}")
    else:
        print("\nEi näyttelijää.")

    query = ("SELECT titles.name FROM titles "
             "INNER JOIN actors_has_titles ON actors_has_titles.titles_id = titles.id "
             "WHERE actors_has_titles.actors_id = (%s);")
    cursor.execute(query, (id,))

    titles = cursor.fetchall()

    if titles:
        actor_titles = ""
        for title in titles:
            actor_titles += title['name'] + ", "
        actor_titles = actor_titles[:-2]
        print("Näyttelee elokuvissa/sarjoissa: " + actor_titles)