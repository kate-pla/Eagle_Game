import random
import math
class Eagle:
    def create_resource():
        ''' Creates the random resource and adds and random number of 
         additional energy points '''
        x = random.randrange(0,100)
        y = random.randrange(0,100)
        energy = random.randrange(1,10)
        return energy,x,y
    def energy_loss(miles, speedlevel):
        ''' Calculates the energy the player loses'''
        loss = speedlevel * (miles/10)
        return loss
    def calcualte_score(total_distance,energy,total_time):
        '''Calculate the score of the player adding the total distance the eagle flew, 
           the energy the eagle has and the total time the eagle spent flying '''
        final_score = (total_distance + energy) -total_time
        return final_score
    def calcuate_distance(x1,y1,x2,y2):
        '''Calcuates the distance the eagle flew from the current 
           point his at to the point the eagles wants to fly'''
        distance= math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return round(distance)
    def calcuate_time(distance, speed):
        '''Calcuates the time it took the eagles to fly to the next point'''
        time = distance/speed
        return time
    def calcualte_rest(energy,rest_hours):
        '''Calcuates how much energy the eagles gets from resting'''
        energy = energy + rest_hours
        return energy
    def add_player(points,eaglename):
        '''Adds the palyers score to the text file and sorts them from 
          highest score to lowest score'''
        with open("players.txt","r") as file:
            lines = file.readlines()
            player = f"{points}:{eaglename}\n"
            lines.append(player)
            lines.sort(reverse=True)
            with open("players.txt","w") as file:
                file.writelines(lines)


#Initialize the values 
energy = 250
x1 = 0
y1 = 0
total_distance= 0
distance = 0
total_time = 0 
time = 0 
add_energy =0
num = 0
xr= 0
yr=0
#Ask User to input an Eagle name
eagle_name = input("Eagle Name: ")
for i in range(1,6):
    print(f"You are in round {i}/25")
    print(f"You have an energy level of {energy}")
    print(f"You are currently a coordinate {x1},{y1}")
    #Asking the user if they want to fly or rest
    user_input = input("Would you like to rest or fly: ")
    user_input = user_input.lower()
    num = random.randint(0,1)
    #If statment to check if the user choose fly or rest 
    if user_input== "fly":
        # Creating the resource 
        if num <= 0.50:
            resource = Eagle.create_resource()
            xr = resource[1]
            yr = resource[2]
            add_energy = resource[0]
            print(f"There is a resource at({xr},{yr}). You will gain an energy level of {add_energy} ")
        #User inputs where they want to fly 
        coordinate = input("Enter the coordiante you would like to fly to x,y: ")
        coordinate = coordinate.split(",")
        #Get the two coordinates 
        x2 = int(coordinate[0])
        y2 = int(coordinate[1])
        #Checks if the coordiantes are valid
        if x2 <-100 or x2 >100 or y2 <-100 or y2 >100:
            print("invalid coordinate")
            coordinate = input("Enter the coordiante you would like to fly to x,y: ")
        #Users inputs what Speed they want to go 
        speed =input("Enter the speed you would like to go (1-10):")
        speed = int(speed)
        #Adds the energy of the resource 
        if x2 == xr and y2 == yr:
            energy = energy + add_energy
         # Calculate the distance 
        distance = Eagle.calcuate_distance(x1,y1,x2,y2)
        time = Eagle.calcuate_time(distance, speed)
        # calculate energy loss
        energy = energy - Eagle.energy_loss(distance,speed)
        #Update the values 
        x1 += x2
        y1 += y2
        total_distance += distance 
        total_time += round(time)
    elif(user_input.lower() == "rest"):
        rest = input("How many hours do you want to rest(1-10)")
        #Adds the energy to Eagle after resting 
        rest = int(rest)
        energy = Eagle.calcualte_rest(energy,rest)
        total_time += rest
    if energy <=0:
        print("You lose!")
        break
print("You have finished the 25 rounds")
# Calcualte the points
if energy > 0:
    points = Eagle.calcualte_score(total_distance, energy, total_time)
    print(f"You have a score of {points}")
    #Adding the player to the text file 
    Eagle.add_player(points,eagle_name)