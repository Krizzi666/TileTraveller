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
def new_direction(a,b):
    if a == "1,1":
        b = "(N)orth"
    elif a == "1,2":
       b = "(N)orth" +" or "+ "(S)outh" +" or "+ "(E)ast"
    elif a == "1,3":
       b = "(S)outh" +" or "+"(E)ast"
    elif a =="2,1":
        b = "(N)orth"
    elif a =="2,2":
       b = "(S)outh"+" or "+"(W)est"
    elif a =="2,3":
        b ="(E)ast"+" or "+"(W)est"
    elif a =="3,1":
       b = "(N)orth"
    elif a =="3,2":
        b = "(N)orth" +" or "+ "(S)outh"
    elif a =="3,3":
        b = "(W)est"+" or "+"(S)outh"
    return b



current_location_x = 1
current_location_y = 1
current_location = "1,1"


a = 0
b = 0

#The walls
possible_direction = ""

possible_direction = new_direction(current_location,possible_direction)

prompt(possible_direction)
user_input = input("Direction: ")

direction = str(user_input)

north = "Nn"
south = "Ss"
east = "Ee"
west = "Ww"


#Player interaction

while current_location_x > 0 and current_location_x <= 3 and current_location_y > 0 and current_location_y <= 3:
    if direction in north and "(N)orth" in possible_direction:
        current_location = str(current_location_x) +","+str(directionup(a,current_location_y))
        current_location_y += 1
        possible_direction = new_direction(current_location,possible_direction)
    elif direction in south and "(S)outh" in possible_direction:
        current_location = str(current_location_x)+","+str(directiondown(a,current_location_y))
        current_location_y -= 1
        possible_direction = new_direction(current_location,possible_direction)
    elif direction in east and "(E)ast" in possible_direction:
        current_location = str(directionright(current_location_x,b))+","+str(current_location_y)
        current_location_x += 1
        possible_direction = new_direction(current_location,possible_direction)
    elif direction in west and "(W)est" in possible_direction:
        current_location = str(directionleft(current_location_x,b))+","+str(current_location_y)
        current_location_x -= 1
        possible_direction = new_direction(current_location,possible_direction)
    else:
        print("Invalid direction, try again") 
    if current_location == "3,1":
        winner()
        break
    prompt(possible_direction)
    direction = input("Direction: ")

    

