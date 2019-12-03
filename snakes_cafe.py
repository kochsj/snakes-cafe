# print intro message
print('', end='\n'*2)
print('*'*43)
print('**', ' '*4, 'Welcome to the Snakes Cafe!', ' '*4,'**' )
print('**', ' '*4, 'Please see our menu below:', ' '*5,'**' )
print('**', ' '*37, '**')
print('**', ' '*2, 'To quit at any time, type "quit"', ' ', '**')
print('*'*43, end='\n'*4)
# print the menu
print('Appetizers')
print('-'*9)
print('Wings')
print('Cookies')
print('Spring Rolls', end='\n'*2)

print('Entrees')
print('-'*9)
print('Salmon')
print('Steak')
print('Meat Tornado')
print('A Literal Garden', end='\n'*2)

print('Desserts')
print('-'*9)
print('Ice Cream')
print('Cake')
print('Pie', end='\n'*2)

print('Drinks')
print('-'*9)
print('Coffee')
print('Tea')
print('Unicorn Tears', end='\n'*4)

# prompt the user to select a food to order
print('*'*43)
print('**', ' '*3,'What would you like to order?', ' '*3, '**')
print('*'*43, end='\n'*2)

# create snake cafe dictionary
Snake_cafe = {
    'wings' : 0,
    'cookies' : 0,
    'spring rolls' : 0,
    'salmon' : 0,
    'steak' : 0,
    'meat tornado' : 0,
    'a literal garden' : 0,
    'ice cream' : 0,
    'cake' : 0,
    'pie' : 0,
    'coffee' : 0,
    'tea' : 0,
    'unicorn tears' : 0
}

while True:
    order = input('Order: ')
    if order == 'quit':
        break
    if order.lower() in Snake_cafe:
        if Snake_cafe[order.lower()] == 0:
            print('**', f'1 order of {order} have been added to your meal', '**')
        else:
            print('**', f'{Snake_cafe[order] += 1} order of {} have been added to your meal', '**')    

