def ten_most_liked(cursor):

    # Haetaan 10 tykätyintä nimikettä.
    query = ("SELECT titles.name, AVG(ratings.rating) AS avg_rating "
             "FROM ratings "
             "INNER JOIN titles ON ratings.titles_id = titles.id "
             "GROUP BY titles.name "
             "ORDER BY avg_rating DESC LIMIT 10;")
    cursor.execute(query)

    titles = cursor.fetchall()
    print("\n10 suosituinta:\n")
    if titles:
        for title in titles:
            print(title['name'].strip(",()") + "   " + str(round(title['avg_rating'], 1)) + "/5")
    else:
        print("Ei tykkäyksiä.")