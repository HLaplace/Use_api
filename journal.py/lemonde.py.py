import feedparser

entry = feedparser.parse("https://www.lemonde.fr/rss/une.xml")

def actualite(numero):
    test_2 = len(entry['entries'][numero]['title'])
    test = test_2 // 2
    tab_temp = []
    tab_temp_2 = []

    for i in range(0, test):
        tab_temp.append(entry['entries'][numero]['title'][i])
    temp = "".join(tab_temp)
    print(temp)

    for j in range(test, test_2):
        tab_temp_2.append(entry['entries'][numero]['title'][j])
    temp_2 = "".join(tab_temp_2)
    print(temp_2)

    #print(entry['entries'][numero]['description'])

actualite(0)