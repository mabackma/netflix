import os
import mysql.connector

from items.addactor import add_actor_to_title
from items.deleteactor import delete_actors_from_title
from items.deletebyid import delete_ratings_by_title_id
from items.edit import edit as edit_title
from actors.edit import edit as edit_actor
from actors.add import add as add_actor
from items.add import add as add_title
from items.addrating import add_rating
from items.all import items_all
from items.bycategory import by_category
from actors.delete import delete as delete_actor
from items.delete import delete as delete_item
from items.tenmostliked import ten_most_liked
from items.tenmostwatched import ten_most_watched
from items.byuser import by_user
from items.byactor import by_actor
from items.byid import by_id as title_by_id
from actors.all import actors_all
from actors.byitem import actors
from actors.byid import by_id as actor_by_id

connection = None
cursor = None

while True:
    os.system('cls')
    choice = input("*******************************************************************\n"
                   "*                             NETFLIX                             *\n"
                   "*******************************************************************\n"
                   "\nAnna toiminto (syötä numero):\n\n"
                   "1. Listaa kaikki nimikkeet.\n"
                   "2. Listaa nimike kategoriasta.\n"
                   "3. Listaa 10 suosituinta nimikettä.\n"
                   "4. Listaa 10 eniten katsottua nimikettä.\n"
                   "5. Listaa tietyn käyttäjän katsomat/pelaamat/kuuntelemat nimikkeet.\n"
                   "6. Listaa elokuvat/sarjat näyttelijän mukaan.\n"
                   "7. Listaa yksittäisen nimikkeen tiedot id:llä haettuna.\n"
                   "8. Listaa kaikki näyttelijät.\n"
                   "9. Listaa tietyn nimikkeen kaikki näyttelijät.\n"
                   "10. Listaa näyttelijän tiedot id:llä haettuna.\n\n"
                   "11. Lisää arvostelu nimikkeelle.\n"
                   "12. Poista arvostelu nimikkeeltä.\n"
                   "13. Lisää nimike.\n"
                   "14. Lisää näyttelijä.\n"
                   "15. Lisää näyttelijä nimikkeeseen.\n"
                   "16. Poista näyttelijä nimikkeestä.\n"
                   "17. Poista näyttelijä.\n"
                   "18. Poista nimike.\n"
                   "19. Muokkaa nimikettä.\n"
                   "20. Muokkaa näyttelijää.\n\n"
                   "Q. Sulje ohjelma.\n\n"
                   "VALINTA: ")

    try:
        connection = mysql.connector.connect(user='root', database='netflix')

        if choice == str(1):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                items_all(cursor)
        if choice == str(2):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                by_category(cursor)
        if choice == str(3):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                ten_most_liked(cursor)
        if choice == str(4):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                ten_most_watched(cursor)
        if choice == str(5):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                by_user(cursor)
        if choice == str(6):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                by_actor(cursor)
        if choice == str(7):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                title_by_id(cursor)
        if choice == str(8):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                actors_all(cursor)
        if choice == str(9):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                actors(cursor)
        if choice == str(10):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                actor_by_id(cursor)

        if choice == str(11):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                add_rating(cursor)
            connection.commit()
        if choice == str(12):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                delete_ratings_by_title_id(cursor)
            connection.commit()
        if choice == str(13):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                add_title(cursor)
            connection.commit()
        if choice == str(14):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                add_actor(cursor)
            connection.commit()
        if choice == str(15):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                add_actor_to_title(cursor)
            connection.commit()
        if choice == str(16):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                delete_actors_from_title(cursor)
            connection.commit()
        if choice == str(17):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                delete_actor(cursor)
            connection.commit()
        if choice == str(18):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                delete_item(cursor)
            connection.commit()
        if choice == str(19):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                edit_title(cursor)
            connection.commit()
        if choice == str(20):
            with connection.cursor(prepared=True, dictionary=True) as cursor:
                edit_actor(cursor)
            connection.commit()
        if choice == "Q" or choice == "q":
            break

        input("\n--------------------------------\nPaina Enter jatkaaksesi.")

    except mysql.connector.Error as err:
        print()
        print(err)
        input("\n--------------------------------\nPaina Enter jatkaaksesi.")

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()
