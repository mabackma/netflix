def by_user(cursor):

    user = input("\nAnna käyttäjätunnus (sähköpostiosoitteesi): ")

    # Haetaan tietyn käyttäjän tilaamat nimikkeet.
    query = ("SELECT titles.name "
             "FROM titles "
             "INNER JOIN subscription_types_has_titles ON titles.id = subscription_types_has_titles.titles_id "
             "INNER JOIN subscription_types "
             "ON subscription_types_has_titles.subscription_types_id = subscription_types.id "
             "INNER JOIN subscriptions ON subscription_types.id = subscriptions.subscription_types_id "
             "INNER JOIN users ON subscriptions.id = users.subscriptions_id "
             "WHERE users.email = (%s);")
    cursor.execute(query, (user,))

    titles = cursor.fetchall()
    if titles:
        print(f"\nKäyttäjän {user} nimikkeet:\n")
        for title in titles:
            print(title['name'].strip(",()"))
    else:
        print("\nEi nimikkeitä.")