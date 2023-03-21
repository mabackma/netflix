def delete(cursor):

    # Näytetään kaikki nimikkeet
    query = ("SELECT id, name FROM titles;")
    cursor.execute(query)

    titles = cursor.fetchall()

    if titles:
        print("\nKaikki nimikkeet:")
        for title in titles:
            print(str(title['id']) + ". " + title['name'])
    else:
        print("\nEi nimikkeitä.")

    id = input("\nAnna poistettavan nimikkeen id: ")

    # Poistetaan nimike tietokannasta.
    query = ("DELETE FROM titles WHERE id = (%s)")
    cursor.execute(query, (id,))

    print(f"\nNimike {id} poistettu tietokannasta.")