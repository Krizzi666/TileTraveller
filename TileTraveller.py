# The Github repository can be found at:
# https://github.com/Krizzi666/TileTraveller

# def directionup(x,y):
#     return y + 1
# def directiondown(x,y):
#     return y - 1
# def directionright(x,y):
#     return x + 1
# def directionleft(x,y):
#     return x - 1
# def prompt(a):
#     print("You can travel: ",a)
# def winner():
#     print("Victory")
# def new_direction(a,b):
    # if a == "1,1":
    #     b = "(N)orth"
    # elif a == "1,2":
    #    b = "(N)orth" +" or "+ "(S)outh" +" or "+ "(E)ast"
    # elif a == "1,3":
    #    b = "(S)outh" +" or "+"(E)ast"
    # elif a =="2,1":
    #     b = "(N)orth"
    # elif a =="2,2":
    #    b = "(S)outh"+" or "+"(W)est"
    # elif a =="2,3":
    #     b ="(E)ast"+" or "+"(W)est"
    # elif a =="3,1":
    #    b = "(N)orth"
    # elif a =="3,2":
    #     b = "(N)orth" +" or "+ "(S)outh"
    # elif a =="3,3":
    #     b = "(W)est"+" or "+"(S)outh"
    # return b



current_location_x = 1
current_location_y = 1
current_location = "1,1"


a = 0
b = 0

#The walls
possible_direction = ""

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

print("You can travel: ",possible_direction)
user_input = input("Direction: ")

direction = str(user_input)

north = "Nn"
south = "Ss"
east = "Ee"
west = "Ww"


#Player interaction

while current_location_x > 0 and current_location_x <= 3 and current_location_y > 0 and current_location_y <= 3:
    if direction in north and "(N)orth" in possible_direction:
        current_location_y += 1
        current_location = str(current_location_x) +","+ str(current_location_y)
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
        current_location_y -= 1
        current_location = str(current_location_x) +","+ str(current_location_y)
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
    elif direction in east and "(E)ast" in possible_direction:
        current_location_x += 1
        current_location = str(current_location_x) +","+ str(current_location_y)
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
        current_location_x -= 1
        current_location = str(current_location_x) +","+ str(current_location_y)
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
        print("Not a valid direction!") 
    if current_location == "3,1":
        print("Victory")
        break
    print("You can travel: ",possible_direction)
    direction = input("Direction: ")

    

