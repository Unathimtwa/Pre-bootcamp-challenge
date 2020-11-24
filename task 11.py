def common_letters(name, country):
     word1 = set(name)
     word2 = set(country)
     lst = word1 & word2
     return lst

print(common_letters("Nozuko", "New zoloka"))

