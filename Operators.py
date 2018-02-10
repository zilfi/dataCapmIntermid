#COMPARISON OPERATORS
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?4
print(my_kitchen>10 and my_kitchen<18)
# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen<14 or my_kitchen>17)
# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen*2 < 3*your_kitchen)

#BOOLEAN OPERATORS 
#np.logical_and()___np.logical_not()_____np.logical_or()____________________


#IF,ELSEIF,ESLE
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :

