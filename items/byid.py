from actors.byitem import show_actors_in_title
from items.all import print_titles, show_titles


def by_id(cursor):

    show_titles(cursor)
    id = input("\nAnna nimikkeen id, jonka tiedot haluat nähdä: ")

    # Näytetään nimikkeen tiedot.
    show_title_details(cursor, id)

    # Näytetään nimikkeen näyttelijät.
    print("Näyttelijät:", end=" ")
    show_actors_in_title(cursor, id, False)

    # Näytetään nimikkeen arvostelut.
    show_all_ratings(cursor, id, False)


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
    else:
        print("\nNimikettä ei löytynyt.")


def show_all_ratings(cursor, id, is_id):

    query = ("SELECT users.id AS user_id, users.email, ratings.rating FROM users "
             "INNER JOIN ratings ON users.id = ratings.users_id "
             "INNER JOIN titles ON ratings.titles_id = titles.id "
             "WHERE titles.id = (%s);")
    cursor.execute(query, (id,))

    ratings = cursor.fetchall()
    amount = 0
    rating_sum = 0
    if ratings:
        print("\nArvostelut:")
        for rating in ratings:
            amount += 1
            rating_sum += rating['rating']
            if is_id:
                print(f"{rating['user_id']}. {rating['email']}: {rating['rating']}")
        print(f"Keskiarvo: {round(rating_sum / amount, 2)}")
    else:
        print("\nEi arvosteluja.\n")