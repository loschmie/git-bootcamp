fruit = {'lemon': 'yellow citrus fruit',
         'banana': 'good for mood',
         'lime': 'a sour green citrus',
         'orange': 'orange citrus fruit',
         'apple': 'good for cider',
         'grape': 'a small sweet fruit'}

while True:
    dict_key = input('Please enter a fruit: ')
    if dict_key == 'quit':
        break
    description = fruit.get(dict_key, "We don't have a {}".format(dict_key))
    print(description)
