def shopping():
    shopping_list = []
    adding = True
    while adding == True:
        shopping_list.append(input("What do you need at the store?\n"))
        list_length = len(shopping_list) - 1
        if shopping_list[list_length] == "DONE":
            adding = False
            print("You need to pick up:\n")
            shopping_list.remove("DONE")
            for item in shopping_list:
                print(item)
            break
            
shopping()