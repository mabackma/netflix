from items.all import show_titles


def actors(cursor):

    show_titles(cursor)

    id = input("\nAnna elokuvan tai sarjan id, jonka näyttelijät haluat nähdä: ")

    query = ("SELECT name FROM titles "
             "WHERE titles.id = (%s)")
    cursor.execute(query, (id,))

    title = cursor.fetchone()

    if title:
        print("\nNäyttelijät nimikkeessä '" + title['name'] + "':")
    else:
        print("Nimikettä ei löytynyt.")

    show_actors_in_title(cursor, id, False)


def show_actors_in_title(cursor, id, is_id):

    query = ("SELECT actors.id, actors.first_name, actors.last_name "
             "FROM actors "
             "INNER JOIN actors_has_titles ON actors.id = actors_has_titles.actors_id "
             "INNER JOIN titles ON actors_has_titles.titles_id = titles.id "
             "WHERE titles.id = (%s)")
    cursor.execute(query, (id,))

    actors_in_title = cursor.fetchall()

    with_id = ""
    without_id = ""
    if actors_in_title:
        for actor in actors_in_title:
            with_id += str(actor['id']) + ". " + actor['first_name'] + " " + actor['last_name'] + "\n"
            without_id += actor['first_name'] + " " + actor['last_name'] + ", "
        if is_id:
            print(with_id)
        else:
            without_id = without_id[:-2]
            print(without_id)
    else:
        print("Ei näyttelijöitä.")