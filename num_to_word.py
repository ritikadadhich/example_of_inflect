import inflect
g=int(input("enter the word: "))
    
p=inflect.engine()
h=p.number_to_words(g)
print(h)
