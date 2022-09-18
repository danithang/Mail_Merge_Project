# creating a variable with the string we want to replace with an actual name
PLACEHOLDER = "[name]"

# opening the folders to get to invite_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    # putting names_file in a variable and reading it as a list containing each line in the file as a list item
    names = names_file.readlines()

# opening the folders to get to starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter_file:
    # reading the file
    letter_contents = letter_file.read()
    # for loop to go through each name in names variable and replacing PLACEHOLDER variable with a different name
    for name in names:
        # stripping the new line after the name
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # opening Readytosend and creating new letter for each name changing the mode to write
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            # writing a letter for each different name
            completed_letter.write(new_letter)

