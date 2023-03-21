from datetime import datetime
from actors.all import actors_all
from actors.byid import actor_details


def edit(cursor):

    actors_all(cursor)
    actor_id = input("\nAnna muokattavan näyttelijän id: ")

    actor_details(cursor, actor_id)

    # Haetaan kaikki nimikkeen tiedot id:n perusteella.
    query = ("SELECT * FROM actors WHERE id = (%s);")
    cursor.execute(query, (actor_id,))
    result = cursor.fetchone()
    current_fn = result['first_name']
    current_ln = result['last_name']
    current_birth_date = result['birth_date']

    # Pyydetään näyttlijän uudet tiedot.
    new_fn = input("\nUusi etunimi: ")
    new_ln = input("Uusi sukunimi: ")
    new_birth_date = input("Uusi syntymäpäivä (YYYY-MM-DD): ")

    if new_fn.strip() == "":
        new_fn = current_fn
    if new_ln.strip() == "":
        new_ln = current_ln
    if new_birth_date.strip() == "":
        new_birth_date = current_birth_date
    else:
        new_birth_date = datetime.strptime(new_birth_date, "%Y-%m-%d").date()

    update_query = ("UPDATE actors SET first_name = (%s), last_name = (%s), birth_date = (%s) "
                    "WHERE id = (%s)")
    cursor.execute(update_query, (new_fn, new_ln, new_birth_date, actor_id))

    print(f"\nNäyttelijän {actor_id} tietoja päivitetty:")
    actor_details(cursor, actor_id)