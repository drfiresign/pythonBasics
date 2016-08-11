# make/load a list to hold our items
todo_list = []

# print out instructions on how to use the app
print("\nWhat should we do today?")

# HELP function
def help_list():
    print("""
Enter 'LOAD' to load the previous list.
Enter 'DONE' to stop adding items.
Enter 'SHOW' to see what's on the list.
Enter 'HELP' to see these commands again.
""")


# SHOW function
def show_list():
    print("Here's your list:")

    for item in todo_list:
        print(item)

# ADD to list
def add_to_list(new_item):
    # add new items to our list
    todo_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(todo_list)))

# SAVE function
def save_list():
    with open('todo_list_storage.txt', 'w') as f:
        for item in todo_list:
            f.write(item + '\n')
        f.close()
    print("Your current list has been saved.")

# LOAD old file list
def load_list():
    global todo_list
    with open('todo_list_storage.txt', 'r') as f:
        todo_list.append(f.read())
        f.close()
        if todo_list[0] is "":
            todo_list = []
    print("Your previous List has been loaded.")

# MAIN FUNCTIONALITY
def main():
    help_list()

    while True:
        # ask for new items
        new_item = input("> ")
        # be able to quit the app
        if new_item == "DONE":
            break
        elif new_item == "SHOW":
            show_list()
            continue
        elif new_item == "HELP":
            help_list()
            continue
        elif new_item == "SAVE":
            save_list()
            continue
        elif new_item == "LOAD":
            load_list()
            continue
        add_to_list(new_item)

    show_list()

main()