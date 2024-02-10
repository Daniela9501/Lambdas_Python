#List of employees names
names_list = ['Frank Harrelson', 'Bob Sharles','Bob Tranklin','Bob Grody', 'Hank Charles', 'Bob Rarrelson',
              'Mack Slobson', 'John Jonones', 'Rob Wranklin', 'Tom Simpsonian', 'Rob Rearrelson', 'John Moodys', 
              'Frank Shones', 'John Harrelson','Frank Quhorles', 'Tom Pharles', 'Frank Fwanklin', 'Frank Charleston', 
              'John Arles', 'John Georanklin', 'Frank Dobsonsoson', 'Diane Johnston', 'Dob Scone', 'Michael Scarn', 
              'Goldie Hawn', 'Billie Holliday', 'Woody Harrelson', 'Arthur Rubinstein', 'Thomas Edison', 'Robert Goulet']

#Sorting the names_list by last name using a lambda function
#The lambda function splits each name and uses the last element (last name) as the key for sorting
print(sorted(names_list, key=lambda name:name.split()[-1]))

#Creating a list of "five and two" usernames
#This lambda function takes each name, split it, and then constructs the username
#By taking the first 5 characters of the last name and the first 2 characteres of the first name
print(list(map(lambda name: name.split()[-1][:5] + name.split()[0][:2], names_list)))
