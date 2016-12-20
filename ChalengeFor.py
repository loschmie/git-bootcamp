##print('Please enter the ip address: ')
##ip_address = input()
##dots = '...'
##if len(ip_address) not in range(8, 16) or ip_address == '0.0.0.0' or ip_address not in ('.0123456789'):
##    print('That is not the valid ip address')
print('please enter a ip address:')
ip_address = input()
first_number = ''
second_number = ''
third_number = ''
fourth_number = ''
stop_point = 0
for char in ip_address:
    if char not in '.' and char in '0123456789':
        first_number += char
    else:
        stop_point = len(first_number)
        break

#print(stop_point)

for char in range(stop_point + 1, len(ip_address)):
    if ip_address[char] not in '.' and ip_address[char] in '0123456789':
        second_number += ip_address[char]
    else:
        stop_point += len(second_number)
        break

#print(stop_point)

for char in range(stop_point + 1, len(ip_address)):
    if ip_address[char] not in '.' and ip_address[char] in '0123456789':
        print(stop_point)
        third_number += ip_address[char]
        print(third_number)
