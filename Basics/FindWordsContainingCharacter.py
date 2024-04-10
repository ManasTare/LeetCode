words = ["leet","code"]
x = "e"
new_word = []
for index , word in enumerate(words):
    new_word = list(word)
    for i in new_word:
        if(x==i):
            print(index)
