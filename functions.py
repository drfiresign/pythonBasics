def hows_the_parrot():
    print("He's pining for the fjords!")
    
hows_the_parrot()

def lumberjack(name, pronoun):
    if pronoun.lower() in ["male", "he", "him", "his", "boy", "man", "dude", "guy"]:
        pronoun = "he's"
        pronoun1 = "he works"
    elif pronoun.lower() in ["female", "her", "she", "woman", "lady", "girl", "hers", "her\'s"]:
        pronoun = "she's"
        pronoun1 = "she works"
    else:
        pronoun = "they're"
        pronoun1 = "they work"
    
    if name.lower() == "dylan":
        print("{}'s a lumberjack and {} OK!".format(name, pronoun))
        
    else:
        print("{} sleeps all night and {} all day!".format(name, pronoun1))
        
lumberjack("Dylan", "dude")
lumberjack("Jesse", "lady")

def average(num1, num2):
    return ((num1 + num2)/2)

avg = average(2, 8)
print(avg)