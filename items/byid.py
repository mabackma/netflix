from items.all import print_titles, show_titles


def by_id(cursor):

    show_titles(cursor)
    id = input("\nAnna nimikkeen id: ")

    show_title_details(cursor, id)
    show_all_ratings(cursor, id)


def show_title_details(cursor, id):

    # Haetaan kaikki nimikkeen tiedot id:n perusteella.
    query = ("SELECT t.id, t.name, t.year, t.running_time, t.description, t.age_rating, mt.type AS media_type "
             "FROM titles t "
             "INNER JOIN media_types mt ON t.media_types_id = mt.id "
             "WHERE t.id = (%s);")
    cursor.execute(query, (id,))

    title = cursor.fetchall()
    if title:
        print_titles(title)
        print()
    else:
        print("\nNimikettä ei löytynyt.")


def show_all_ratings(cursor, id):

    query = ("SELECT users.email, ratings.rating FROM users "
             "INNER JOIN ratings ON users.id = ratings.users_id "
             "INNER JOIN titles ON ratings.titles_id = titles.id "
             "WHERE titles.id = (%s);")
    cursor.execute(query, (id,))

    ratings = cursor.fetchall()
    amount = 0
    rating_sum = 0
    if ratings:
        print("Arvostelut:")
        for rating in ratings:
            amount += 1
            rating_sum += rating['rating']
            print(f"{rating['email']}: {rating['rating']}")
        print(f"\nKeskiarvo: {round(rating_sum / amount, 2)}")
    else:
        print("\nEi arvosteluja.\n")