from items.byid import show_all_ratings


def delete_ratings_by_title_id(cursor):

    query = ("SELECT titles.id AS id, titles.name AS name, ratings.rating AS rating "
             "FROM titles "
             "INNER JOIN ratings ON titles.id = ratings.titles_id;")
    cursor.execute(query)

    id_tuple = cursor.fetchall()

    print()
    shown_titles = set()
    for item in id_tuple:
        if item['rating'] and item['id'] not in shown_titles:
            print(f"{item['id']}. {item['name']}:")
            show_all_ratings(cursor, item['id'], False)
            shown_titles.add(item['id'])
            print()

    id_title = input("Anna nimikkeen id, josta haluat poistaa arvostelun: ")

    show_all_ratings(cursor, id_title, True)

    user_id = input("\nAnna käyttäjän id jonka arvostelun haluat poistaa: ")

    query = ("DELETE FROM ratings "
             "WHERE titles_id = (%s) AND users_id = (%s)")
    cursor.execute(query, (id_title, user_id))

    print(f"\nPoistetaan käyttäjän {user_id}. arvostelu valitsemastasi nimikkeestä.")