def by_category(cursor):

    query = ("SELECT id, name FROM categories;")
    cursor.execute(query)

    categories_tuple = cursor.fetchall()

    categories = ""
    for cat in categories_tuple:
        categories += f"\n{cat['id']}. {cat['name']}"

    # Näytetään kategoriat.
    print(categories)
    category = input("\nAnna kategorian id: ")

    # Haetaan nimikkeet tietystä kategoriasta.
    query = ("SELECT titles.name "
             "FROM categories "
             "INNER JOIN categories_has_titles ON categories.id = categories_has_titles.categories_id "
             "INNER JOIN titles ON categories_has_titles.titles_id = titles.id "
             "WHERE categories.id = (%s);")
    cursor.execute(query, (category,))

    titles = cursor.fetchall()

    if titles:
        print('\nNimikkeet kategoriassa:\n')
        for title in titles:
            print(title['name'].strip(",()"))
    else:
        print("\nKategoriassa ei ole nimikkeitä.")

    if cursor is not None:
        cursor.close()