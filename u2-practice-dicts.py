# Basic syntax of a dictionary:
books = {'Tim Ferriss': 'The 4-Hour Work Week', 'Jocko Willink' : 'Discipline Equals Freedom', 'Jordan Peterson' : '12 Rules for Life'}

# Packing data into a dictionary:
def packer(**kwargs):
    print(kwargs)

packer(name="Tim Ferriss", books=4, hair=None)

# Unpacking a dictionary:
def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi, NoName!")

unpacker(**{"last_name": "Ferriss", "first_name": "Tim"})

# Another example of unpacking a dictionary:
dict = {"name": "Tim", "surname": "Ferriss"}
print("Hello there, nice to meet you {name} {surname}!".format(**dict))

# This prints the authors of the books:
for author in books:
    print(author)

# This prints the names of the books:
for author in books:
    print(books[author])

# The .key() method returns an iterable of all of the keys in a dictionary:
for key in books.keys():
    print(key + "!")

# The .values() method returns an iterable of all of the values in a dictionary:
for value in books.values():
    print(value + "!")

# The .items() method returns the combination of keys and values in a dictionary:
for item in books.items():
    print(item)