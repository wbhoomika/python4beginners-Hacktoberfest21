# reading invited names and adding them into the list...
with open('./Input/Names/invited_names.txt') as invited_people:
    invited_people_list = invited_people.readlines()

# for each person,
for person in invited_people_list:
    with open('Input/Letters/starting_letter.txt') as letter:
        # creating new string with replaced name,
        letter_content = letter.read().replace('[name]', person)

# saving files with the content.
    with open(f'Output/ReadyToSend/letter_to_{person}.txt', 'w') as ready_letter:
        ready_letter.write(letter_content)
