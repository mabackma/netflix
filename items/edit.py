from items.all import show_titles
from items.byid import show_title_details


def edit(cursor):

    show_titles(cursor)
    title_id = input("\nAnna muokattavan nimikkeen id: ")

    show_title_details(cursor, title_id)

    # Haetaan kaikki nimikkeen tiedot id:n perusteella.
    query = ("SELECT * FROM titles WHERE id = (%s);")
    cursor.execute(query, (title_id,))
    result = cursor.fetchone()
    current_name = result['name']
    current_year = result['year']
    current_running_time = result['running_time']
    current_description = result['description']
    current_age_rating = result['age_rating']

    # Pyydetään uudet tiedot nimikkeeseen.
    new_name = input("\nUusi nimike: ")
    new_year = input("Uusi julkaisuvuosi: ")
    new_running_time = input("Uusi kesto minuuteissa: ")
    new_description =  input("Uusi kuvaus: ")
    new_age_rating = input("Uusi suositusikäraja: ")

    if new_name.strip() == "":
        new_name = current_name
    if new_year.strip() == "":
        new_year = current_year
    if new_running_time.strip() == "":
        new_running_time = current_running_time
    if new_description.strip() == "":
        new_description = current_description
    if new_age_rating.strip() == "":
        new_age_rating = current_age_rating

    update_query = ("UPDATE titles SET name = (%s), year = (%s), running_time = (%s), "
                    "description = (%s), age_rating = (%s) "
                    "WHERE id = (%s)")
    cursor.execute(update_query, (new_name, new_year, new_running_time, new_description,
                                  new_age_rating, title_id))

    print(f"\nNimike {title_id} päivitetty:")
    show_title_details(cursor, title_id)