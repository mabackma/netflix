from actors.all import actors_all


def delete(cursor):

    # Näytetään kaikki näyttelijät.
    actors_all(cursor)
    id = input("\nAnna poistettavan näyttelijän id: ")

    # Poistetaan näyttelijä tietokannasta.
    query = ("DELETE FROM actors WHERE id = (%s)")
    cursor.execute(query, (id,))

    print(f"\nNäyttelijä {id} poistettu tietokannasta.")