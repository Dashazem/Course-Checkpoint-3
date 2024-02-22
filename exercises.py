# Exercise 1
name = 'Dasha Krylchuk'
messages_count = 26
list_of_followers = ['Anna', 'Maria', 'Elizabeth', 'Chloe']
registered_user = True

print(name)
print(messages_count)
print(list_of_followers)
print(registered_user)

# Exercise 2
first_three_letters = name[:3]
print(first_three_letters)

# Exercise 3
first_element = list_of_followers[0]
print(first_element)

# Exercise 4
new_messages_count = messages_count + 10
print(new_messages_count)

# Exercise 5
last_element = list_of_followers[3]
print(last_element)

# Exercise 6
names = 'harry,alex,susie,jared,gail,conner'         
list_of_names = names.split(',')
print(list_of_names)

# Exercise 7
first_word = name[0:5]
first_word_uppercase = first_word.upper()
new_name = first_word_uppercase + name[5:]
print(new_name)

# Exercise 8
notification = f'You have {messages_count} new messages!'
print(notification)

# Exercise 9
greeting = 'hello world'
print(greeting)