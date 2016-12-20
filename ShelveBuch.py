import shelve
'''
fruit = shelve.open('c:\\Users\\losch\\Desktop\\Fruits.shelve')
fruit['orange'] = 'a sweet, orange, citrus fruit'
fruit['apple'] = 'good for making cider'
fruit['lemon'] = 'a sour, yellow citrus fruit'
fruit['grape'] = 'a small, sweet fruit growing in bunches'
fruit['lime'] = 'a sour, green citrus fruit'

print(fruit['lime'])
print(fruit['grape'])
print("*"*40)
fruit['lime'] = 'great with tequila'

for k, v in sorted(fruit.items()):
    print(k + ': ' + v)

fruit.close()

print(fruit)
'''
##blt = ['bacon', 'lettuce', 'tomato', 'bread']
##beans_on_toast = ['beans', 'bread']
##scrambled_eggs = ['eggs', 'butter', 'milk']
soup = ['can of soup']
##pasta = ['pasta', 'cheese']

##
##with shelve.open('recepies', writeback=True) as recipes:
##    recipes['blt'] = blt
##    recipes['beans_on_toast'] = beans_on_toast
##    recipes['scrambled_eggs'] = scrambled_eggs
##    recipes['soup'] = soup
##    recipes['pasta'] = pasta
##    temp_list = recipes['blt']
##    temp_list.append('butter')
##    recipes['blt'] = temp_list
##    temp_list = recipes['pasta']
##    temp_list.append('tomato')
##    recipes['pasta'] = temp_list
##    recipes['soup'].append('croutons')
##    for snack in recipes:
##        print(snack, recipes[snack])
