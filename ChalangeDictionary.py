locations = {0: 'You are sitting in front of computer learing Python',
             1: 'You are standing at the end of the road before a small brick building',
             2: 'You are at the top of a hill',
             3: 'You are inside the building, a well house for a small stream',
             4: 'You are in a vallley beside a stream',
             5: 'You are in the forest'}

exits = {0:{'Q':0},
         1: {'W': 2, "E": 3, "N": 5, 'S': 4, 'Q': 0},
         2: {'N': 5, 'Q': 0},
         3: {'W': 1, "Q": 0},
         4: {'N': 1, 'W': 2, 'Q': 0},
         5: {'W': 2, 'S': 1, 'Q': 0}}

directions = {'North': 'N',
              'West': 'W',
              'South': 'S',
              'East': 'E',
              'Quit': 'Q'}

loc = 1

while True:
    currentExitKeys = []
    for k, v in directions.items():
        for key in exits[loc].keys():
            if key == v:
                currentExitKeys.append(k)
                    
    availableExits = ', '.join(currentExitKeys)
    print(locations[loc])
    if loc == 0:
        break

    direction = input('Available exits are '+ availableExits.title() + ' ').title()
    while direction not in availableExits:
        direction = input('You need to type "{}" '.format(availableExits.title())).title()
    print()
    if directions[direction] in exits[loc].keys():
        loc = exits[loc][directions[direction]]
                
    else:
        print('You cannot go that way')
        
	
                
