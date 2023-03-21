from actors.byitem import show_actors_in_title
from items.all import show_titles


def delete_actors_from_title(cursor):

    # Näytetään nimikkeet joista voidaan poistaa näyttelijä.
    show_titles(cursor)
    title_id = input("\nAnna nimikkeen id josta haluat poistaa näyttelijä: ")

    # Näytetään näyttelijät joita voidaan poistaa nimikkeestä.
    show_actors_in_title(cursor, title_id)
    actor_id = input("\nAnna poistettavan näyttelijän id: ")

    # Poistetaan näyttelijä nimikkeestä.
    query = ("DELETE FROM actors_has_titles "
             "WHERE titles_id = (%s) AND actors_id = (%s)")
    cursor.execute(query, (title_id, actor_id))

    print(f"\nNäyttelijä poistettu nimikkeestä")