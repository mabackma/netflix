def ten_most_watched(cursor):

    # Haetaan 10 katsotuinta nimikettä.
    query = ("SELECT titles.name, SUM(history.watch_count) AS times_played, media_types.type "
             "FROM history "
             "INNER JOIN titles ON history.titles_id = titles.id "
             "INNER JOIN media_types ON titles.media_types_id = media_types.id "
             "GROUP BY titles.name "
             "ORDER BY times_played DESC LIMIT 10;")
    cursor.execute(query)

    titles = cursor.fetchall()
    print("\n10 katsotuinta:\n")
    if titles:
        for title in titles:
            print(title['name'].strip(",()") + "   (" + str(title['times_played']) + " katselukertaa)")
    else:
        print("Ei nimikkeitä.")