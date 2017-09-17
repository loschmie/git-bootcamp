print('what is your name please?')
name = input()
print("how old are you {} ?".format(name))
age = int(input())
if age in range(18, 31):
    print('Welcome {}'.format(name))
else:
    print('Well {} we have to kindly ask you to leave'.format(name))
    
