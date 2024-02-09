name = input("type your name: ")
print("welcome", name, "to this adventure!")
answer = input("you're in the wilderness and the road has come to an end. you go left or right? ").lower()

if answer == "left":
    answer = input("you've come to a river and you can either walk around or swim across. type walk to walk through or swim to swim across: ")
    if answer == "swim":
        print('you swam across and were eaten by a shark.')
        print("Thank you for trying, " + name) 
    elif answer == "walk":
            print("you walked several miles ran out of energy and died.")
            print("Thank you for trying, " + name) 

elif answer == "right":
    print("Great! Good luck choosing the right path.")
    
else:
    print("not a valid option, you lose.")
    print("Thank you for trying, " + name) 

print("The End") 
