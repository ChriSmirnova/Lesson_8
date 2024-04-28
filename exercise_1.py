roles = {'admin': 'Mike', 'maintainer': 'daria', 'manager': 'luka', 'developer': 'Mark'}
name = input('Enter name:')
found_role = False

for role in roles:
    if name == roles[role]:
        print('Hello,', name)
        found_role = True
        break

if not found_role:
    print('Hello, Guest')
