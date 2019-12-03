# print intro message
print('', end='\n'*2)
print('*'*43)
print('**', ' '*4, 'Welcome to the Snakes Cafe!', ' '*4,'**' )
print('**', ' '*4, 'Please see our menu below:', ' '*5,'**' )
print('**', ' '*37, '**')
print('**', ' '*2, 'To quit at any time, type "quit"', ' ', '**')
print('*'*43, end='\n'*4)
# print the menu
print(' '*13, 'Appetizers')
print(' '*13, '-'*9)
print(' '*13, 'Wings')
print(' '*13, 'Cookies')
print(' '*13, 'Spring Rolls', end='\n'*2)

print(' '*13, 'Entrees')
print(' '*13, '-'*9)
print(' '*13, 'Salmon')
print(' '*13, 'Steak')
print(' '*13, 'Meat Tornado')
print(' '*13, 'A Literal Garden', end='\n'*2)

print(' '*13, 'Desserts')
print(' '*13, '-'*9)
print(' '*13, 'Ice Cream')
print(' '*13, 'Cake')
print(' '*13, 'Pie', end='\n'*2)

print(' '*13, 'Drinks')
print(' '*13, '-'*9)
print(' '*13, 'Coffee')
print(' '*13, 'Tea')
print(' '*13, 'Unicorn Tears', end='\n'*4)

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
        Snake_cafe[order.lower()] += 1
        if Snake_cafe[order.lower()] == 1:
            print('**', f'1 order of {order} have been added to your meal', '**')
        else:
            print('**', f'{Snake_cafe[order.lower()]} order of {order} have been added to your meal', '**')    

