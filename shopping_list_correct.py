# make a list to hold our items
shopping_list = []



# print out instructions on how to use the app
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")
print("Enter 'SHOW' to see what's on the list.")
print("Enter 'HELP' to see these commands again.")

# HELP function
def help_list():
    print("Enter 'DONE' to stop adding items.")
    print("Enter 'SHOW' to see what's on the list.")
    print("Enter 'HELP' to see these commands again.")

# SHOW function
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

while True:
    # ask for new items
    new_item = input("> ")
    # be able to quit the app    
    if new_item == "DONE":
        break
    elif new_item == "SHOW":
        show_list()
    elif new_item == "HELP":
        help_list()
    # add new items to our list
    shopping_list.append(new_item)
# print out the list
print("Here's your list:")

for item in shopping_list:
    print(item)
    