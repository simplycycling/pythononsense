first_name = input('What is your first name? \n')
last_name = input('What is your last name? \n')
print(f'Hello, {first_name} {last_name}!')

