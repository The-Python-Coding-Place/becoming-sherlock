# We have a program that prints a menu in which we can choose to do a number of things
# with a list of names: Either add a name to the list, or make a name uppercase,
# or replace a letter in a name.
# It doesn't quite work, yet

names = ["James", "Kate", "Matthew", "Paul", "Jessica", "Claire"]

print("Would you like to:\n"
      "1. Add a name\n"
      "2. Make name uppercase\n"
      "3. Replace a letter in a name\n")

response = input("——> ")

def show_names():
    '''
    Print out all the current names in the list
    '''
    print()  # adds blank line
    for name in names:
        print(name)
    print()

def choose_name():
    '''
    Allow user to choose a name from the list of names
    :return: choice
    '''
    show_names
    choice = input("Which name do you want to change? [Type in 1 for first name, etc...] ——> ")
    return choice

if response == 1:
    new_name = input("Type in name you wish to add ——> ")
    names.append(new_name)
    show_names
elif response == 2:
    choice = choose_name()
    names[choice].upper()
    show_names
elif response == 3:
    choice = choose_name()
    old = input("Which letter do you wish to replace? ——> ")
    new = input("Which letter do you want to replace it with? ——> ")
    names[choice].replace(old, new)
    show_names
else:
    print("Sorry, you chose an option that doesn't exist")


