from actors.all import actors_all


def by_actor(cursor):

    actors_all(cursor)
    id = input("\nAnna näyttelijän id: ")


    # Haetaan elokuvan nimi näyttelijän id:n perusteella.
    query = ("SELECT titles.name, actors.first_name, actors.last_name "
             "FROM titles "
             "INNER JOIN actors_has_titles ON titles.id = actors_has_titles.titles_id "
             "INNER JOIN actors ON actors_has_titles.actors_id = actors.id "
             "WHERE actors.id = (%s);")
    cursor.execute(query, (id, ))

    titles = cursor.fetchall()
    if titles:
        show_actor = True
        for title in titles:
            if show_actor:
                first_name = title['first_name'].strip(",()")
                last_name = title['last_name'].strip(",()")
                print(f"\nNäyttelijän {first_name} {last_name} nimikkeet:\n")
                show_actor = False
            print(title['name'].strip(",()"))
    else:
        print("\nEi nimikkeitä.")