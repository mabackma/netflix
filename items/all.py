def items_all(cursor):

    # Haetaan kaikki tiedot kaikista nimikkeistä
    query = ("SELECT t.id, t.name, t.year, t.running_time, t.description, t.age_rating, mt.type AS media_type "
             "FROM titles t "
             "INNER JOIN media_types mt ON t.media_types_id = mt.id;")
    cursor.execute(query)

    titles = cursor.fetchall()

    if titles:
        print("\nKaikki nimikkeet:")
        print_titles(titles)
    else:
        print("\nEi nimikkeitä.")


def print_titles(titles):

    for title in titles:
        print(f"\n{title['name']} ({title['year']})\nKesto: {title['running_time']} min\n"
              f"Kuvaus: {title['description']}\n"
              f"Suositusikäraja: {title['age_rating']}\nTyyppi: {title['media_type']}")


def show_titles(cursor):

    query = ("SELECT id, name FROM titles")
    cursor.execute(query, )
    titles = cursor.fetchall()

    print("\nNimikkeet:")
    for title in titles:
        print(f"{title['id']}. {title['name']} ")