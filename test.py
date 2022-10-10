users = [
{'first_name' : 'Michael', 'last_name' : 'Choi'},
{'first_name' : 'John', 'last_name' : 'Supsupin'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
]
for user in users:
    for value in user:
        first_name = user["first_name"]
        last_name = user["last_name"]
        full_name = user["first_name"] + user["last_name"]
