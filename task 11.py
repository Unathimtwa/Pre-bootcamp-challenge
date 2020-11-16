name = input("Please enter your name: ")
country = input("Which country do you live in? : ")
word1 = set(name)
word2 = set(country)
lst = word1 & word2
print(lst)
