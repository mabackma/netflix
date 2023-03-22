from actors.all import actors_all
from items.all import show_titles


def add_actor_to_title(cursor):

    # Näytetään nimikkeet johon voisi lisätä näyttelijän.
    show_titles(cursor)
    id_title = input("\nAnna nimikkeen id johon haluat lisätä näyttelijän: ")

    # Näytetään lista näyttelijöistä joista voidaan valita lisättävä näyttelijä.
    actors_all(cursor)
    is_actor = input(f"\nLöytyykö näyttelijä jonka haluat lisätä listasta (K/E)?\n"
                     f"(Jos näyttelijää ei löydy listasta, niin voit lisätä näyttelijän toiminnolla 14): ")

    # Lisätään nimikkeeseen näyttelijä vain jos se on näyttelijälistassa.
    if is_actor.upper() == "K":
        id_actor = input(f"Anna näyttelijän id kenet haluat lisätä nimikkeeseen {id_title}: ")

        query = ("INSERT INTO actors_has_titles(actors_id, titles_id) "
                 "VALUES((%s), (%s))")
        cursor.execute(query, (id_actor, id_title))

        print("\nNäyttelijä lisätty nimikkeeseen.")
