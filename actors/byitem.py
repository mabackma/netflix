from items.all import show_titles


def actors(cursor):

    show_titles(cursor)

    id = input("\nAnna elokuvan tai sarjan id: ")

    query = ("SELECT name FROM titles "
             "WHERE titles.id = (%s)")
    cursor.execute(query, (id,))

    title = cursor.fetchone()

    if title:
        print("\nNäyttelijät nimikkeessä '" + title['name'] + "':")
    else:
        print("Nimikettä ei löytynyt.")

    show_actors_in_title(cursor, id)


def show_actors_in_title(cursor, id):

    query = ("SELECT actors.id, actors.first_name, actors.last_name "
             "FROM actors "
             "INNER JOIN actors_has_titles ON actors.id = actors_has_titles.actors_id "
             "INNER JOIN titles ON actors_has_titles.titles_id = titles.id "
             "WHERE titles.id = (%s)")
    cursor.execute(query, (id,))

    actors_in_title = cursor.fetchall()

    if actors_in_title:
        for actor in actors_in_title:
            print(str(actor['id']) + ". " + actor['first_name'] + " " + actor['last_name'])
    else:
        print("\nEi näyttelijöitä.")