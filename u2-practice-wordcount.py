def word_count(string):
    word_dict = {}
    word_list = list(string.lower().split())
    for word in word_list:
        word_dict.append([word, word_list.count(word)])
    return dict(word_dict)

string = "I do not think that this example is going to work but I have to try it out and see."
print(word_count(string))