# The Github repository can be found at:
# https://github.com/Krizzi666/TileTraveller

def directionup(x,y):
    return y + 1
def directiondown(x,y):
    return y - 1
def directionright(x,y):
    return x + 1
def directionleft(x,y):
    return x - 1
def prompt(a):
    print("You can travel: ",a)
def winner():
    print("Victory")
# def new_direction(a,b):
#     if a == "1,1":
#         b == "(N)orth"
#     elif a == "1,2":
#        b == "(N)orth" +" or "+ "(S)outh" +" or "+ "(E)ast"
#     elif a == "1,3":
#        b == "(S)outh" +" or "+"(E)ast"
#     elif a =="2,1":
#         b == "(N)orth"
#     elif a =="2,2":
#        b == "(S)outh"+" or "+"(W)est"
#     elif a =="2,3":
#         b =="(E)ast"+" or "+"(W)est"
#     elif a =="3,1":
#        b == "(N)orth"
#     elif a =="3,2":
#         b == "(N)orth" +" or "+ "(S)outh"
#     elif a =="3,3":
#         b == (W)est"+" or "+"(S)outh"
#     return b



current_location_x = 1
current_location_y = 1
current_location = "1,1"


a = 0
b = 0

#The walls

if current_location == "1,1":
    possible_direction = "(N)orth"
elif current_location == "1,2":
    possible_direction = "(N)orth" +" or "+ "(S)outh" +" or "+ "(E)ast"
elif current_location == "1,3":
    possible_direction = "(S)outh" +" or "+"(E)ast"
elif current_location =="2,1":
    possible_direction = "(N)orth"
elif current_location =="2,2":
    possible_direction = "(S)outh"+" or "+"(W)est"
elif current_location =="2,3":
    possible_direction ="(E)ast"+" or "+"(W)est"
elif current_location =="3,1":
    possible_direction = "(N)orth"
elif current_location =="3,2":
    possible_direction = "(N)orth" +" or "+ "(S)outh"
elif current_location =="3,3":
    possible_direction = "(W)est"+" or "+"(S)outh"

prompt(possible_direction)
user_input = input("Input a direction: ")

direction = str(user_input)

north = "Nn"
south = "Ss"
east = "Ee"
west = "Ww"





#Player interaction

while current_location_x > 0 and current_location_x <= 3 and current_location_y > 0 and current_location_y <= 3:
    if direction in north and "(N)orth" in possible_direction:
        current_location = str(current_location_x) +","+str(directionup(a,current_location_y))
        print(current_location)
        current_location_y += 1  
        if current_location == "1,1":
            possible_direction = "(N)orth"
        elif current_location == "1,2":
            possible_direction = "(N)orth" +" or "+ "(S)outh" +" or "+ "(E)ast"
        elif current_location == "1,3":
            possible_direction = "(S)outh" +" or "+"(E)ast"
        elif current_location =="2,1":
            possible_direction = "(N)orth"
        elif current_location =="2,2":
            possible_direction = "(S)outh"+" or "+"(W)est"
        elif current_location =="2,3":
            possible_direction ="(E)ast"+" or "+"(W)est"
        elif current_location =="3,1":
            possible_direction = "(N)orth"
        elif current_location =="3,2":
            possible_direction = "(N)orth" +" or "+ "(S)outh"
        elif current_location =="3,3":
            possible_direction = "(W)est"+" or "+"(S)outh"
    elif direction in south and "(S)outh" in possible_direction:
        current_location = str(current_location_x)+","+str(directiondown(a,current_location_y))
        print(current_location)
        current_location_y -= 1
        if current_location == "1,1":
            possible_direction = "(N)orth"
        elif current_location == "1,2":
            possible_direction = "(N)orth" +" or "+ "(S)outh" +" or "+ "(E)ast"
        elif current_location == "1,3":
            possible_direction = "(S)outh" +" or "+"(E)ast"
        elif current_location =="2,1":
            possible_direction = "(N)orth"
        elif current_location =="2,2":
            possible_direction = "(S)outh"+" or "+"(W)est"
        elif current_location =="2,3":
            possible_direction ="(E)ast"+" or "+"(W)est"
        elif current_location =="3,1":
            possible_direction = "(N)orth"
        elif current_location =="3,2":
            possible_direction = "(N)orth" +" or "+ "(S)outh"
        elif current_location =="3,3":
            possible_direction = "(E)ast"+" or "+"(S)outh"
    elif direction in east and "(E)ast" in possible_direction:
        current_location = str(directionright(current_location_x,b))+","+str(current_location_y)
        print(current_location)
        current_location_x += 1
        if current_location == "1,1":
            possible_direction = "(N)orth"
        elif current_location == "1,2":
            possible_direction = "(N)orth" +" or "+ "(S)outh" +" or "+ "(E)ast"
        elif current_location == "1,3":
            possible_direction = "(S)outh" +" or "+"(E)ast"
        elif current_location =="2,1":
            possible_direction = "(N)orth"
        elif current_location =="2,2":
            possible_direction = "(S)outh"+" or "+"(W)est"
        elif current_location =="2,3":
            possible_direction ="(E)ast"+" or "+"(W)est"
        elif current_location =="3,1":
            possible_direction = "(N)orth"
        elif current_location =="3,2":
            possible_direction = "(N)orth" +" or "+ "(S)outh"
        elif current_location =="3,3":
            possible_direction = "(W)est"+" or "+"(S)outh"
    elif direction in west and "(W)est" in possible_direction:
        current_location = str(directionleft(current_location_x,b))+","+str(current_location_y)
        current_location_x -= 1
        print(current_location)
        if current_location == "1,1":
            possible_direction = "(N)orth"
        elif current_location == "1,2":
            possible_direction = "(N)orth" +" or "+ "(S)outh" +" or "+ "(E)ast"
        elif current_location == "1,3":
            possible_direction = "(S)outh" +" or "+"(E)ast"
        elif current_location =="2,1":
            possible_direction = "(N)orth"
        elif current_location =="2,2":
            possible_direction = "(S)outh"+" or "+"(W)est"
        elif current_location =="2,3":
            possible_direction ="(E)ast"+" or "+"(W)est"
        elif current_location =="3,1":
            possible_direction = "(N)orth"
        elif current_location =="3,2":
            possible_direction = "(N)orth" +" or "+ "(S)outh"
        elif current_location =="3,3":
            possible_direction = "(W)est"+" or "+"(S)outh"
    else:
        print("Invalid direction, try again") 
    if current_location == "3,1":
        winner()
        break
    print(current_location)
    prompt(possible_direction)
    direction = input("Input a direction: ")

        

# elif current_location == "1,1" and direction != north:
#     print("Direction is invalid, try again")

    

