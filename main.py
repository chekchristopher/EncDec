"""
#REMOVE
#---------if,elif,else statement---------#
status = int(input("STATUS: "))

if status == 200:
    print("OK")
elif status == 400:
    print("Bad Request")
elif status == 500:
    print("Internal Server Error")
else:
    print("check other Status")


#---------loop-----------#
string = "security"

for character in string:
    print(character)

computer_assets = ["laptop1", "desktop20", "smartphone03"]

for assets in computer_assets:
    print(assets)


#-----------Range() in loop-----------#
for i in range(0,5,1):
    print(i)

for i in range(5):
    print(i)

i = int(input("what,s your lucky number?"))

while i < 10:
    print(i)

count = 0
login_status = True
while login_status == True:
    print("try again")
    count = count + 1
    if count == 4:
      login_status = False


#---managing loops with 'break'---#
computer_assets = ["laptop1", "desktop20", "smartphone03"]

for assets in computer_assets:
    if assets  == "desktop20":
        break
    print(assets) #the loop stops at "laptop1"


#---managing loops with 'continue'---# 
computer_assets = ["laptop1", "desktop20", "smartphone03"]

for assets in computer_assets:
    if assets == "desktop20":
        continue
    print(assets) #the loop skips "desktop20"

#------infinite loops-----#
if you create a loop that doesn't exists, this is called an infinite loop.
press CTRL-C or CTRL-Z to stop the infinite loop






#----------------------SECTION 2 (FUNCTIONS)-----------------------#
def display_investigation_message():
    print("Investigate Activity")

application_status = "potntial concern"
email_status = "okay"

if application_status == "potential concern":
    print("application_log")
    display_investigation_message()

#--Note: CALLING A FUNCTION INSIDE THE BODY OF ITS FUNCTION CREATES AN INFINITE LOOP--#
#EXAMPLE:
def func1():
    func1()



#-----WORKING WITH VARIABLES IN FUNCTIONS----#
#this requires an understanding of PARAMETERS & ARGUMENTS#
#parameter
def remaining_login_attempts(maximum_attempts, total_attempts):
    print(maximum_attempts - total_attempts)
#a parameter is an object that is included in a function definition for use in that function.
#in the cse above, the variables(maximum_atttempts and total_attempts) are the parameters.

#arguments
#argument is the data brought into a function when it is called.
#EXAMPLE: remianing_login_attempts(3,2). in this example, the integers, 3 & 2 are considered ARGUMENTS



#--------RETURN STATEMENT
#THE RETURN STATEMENT IS NOT A FUNCTION
#example
def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts
remaining_attempts = remaining_login_attempts(3,3)
if remaining_attempts <= 0:
    print("Your account Is Locked")

#example ,  Note that "return statement executes and exits the function"
def greet_employee(name):
    total_string = "welcome" + name
    return total_string


#-----------HOW TO CALL A FUNCTION (local and global variable)
#EXAMPLE
username = "chek"

def identify_user():
    print(username)

identify_user()

#EXAMPLE
username = "elarson"
print("1:" + username)

def greet():
    username = "bmoreno"
    print("2:" + username)
greet()

print("3:" + username)



#-----WORKING WITH BUILT-IN FUNCTIONS-------#
print()
type()
max()
min()
sorted()



#-----IMPORTING MODULE with its in-built functions-----#
import statistics

monthly_failed_attempts = [20,17,178,33,15,21,19,29,32,15,25,19]

mean_failed_attempts = statistics.mean(monthly_failed_attempts)
median_failed_attempts = statistics.median(monthly_failed_attempts)


print("mean:", mean_failed_attempts)
print("median:", median_failed_attempts)


#-----IMPORTING SPECIFIC FUNCTIONS FROM A MODULE-----#
from statistics import mean,median

monthly_failed_attempts = [20,17,178,33,15,21,19,29,32,15,25,19]

mean_failed_attempts = mean(monthly_failed_attempts)
median_failed_attempts = median(monthly_failed_attempts)


print("mean:", mean_failed_attempts)
print("median:", median_failed_attempts)
#REMOVE
"""




#--------------------------STRINGS & THE SECURITY ANALYST-------------------#
"""
INDEX is a number assigned to every element in a sequence that indicates its position.
With stings , this means that each character iin the string has its own index.
indexx startis counting from 0, example:
"h32rb17" :
h       0
3       1
2       2
r       3
b       4
1       5
7       5
"""

"""
#REMOVE
device_id = "h32rb17"
print("h32rb17"[0])
print(device_id[0])
#the above examples will give you the same result
print(device_id[0:3]) #gives you the first 3 elements of the string
#REMOVE
"""
#-----string functions and methods
#A method is a function that belongs to a specific data type

"""
str() function converts its input object into a string:
      Example: device_id = str(19092839)
      
len() function returns the number of elements in an object
      Example: 
      device_id_length = len(1909283)
      if device_id_length == 7:
         print("Correct count")

.upper() method returns a copy of the string in UPPERCASE
      Example: "Infromation Technology".upper()

.lower() method returns a copy of the string in LOWERCASE
      Example: "Infromation Technology".lower()

.index() method finds the occurence of the input in a string and return the location
         Example: print("h32rb17".index("r"))
"""
"""
#REMOVE
print("h32rb17".index("r"))
#REMOVE
"""



"""
#REMOVE
#--------------------------LISTS & THE SECURITY ANALYST-------------------#
username_list = ["elaarson", "fgarcia", "tshah", "sgilmore"]

print(username_list[2])
print(username_list[0:2])

#-----Changing the elements in a  list
#Note that strings are IMMUTABLE(CAN NOT BE CHANGED)
#But lists are MUTABLE
username_list = ["elaarson", "fgarcia", "tshah", "sgilmore"]

username_list[1] = "bmoreno" 
print(username_list)
#REMOVE
"""

#----------list methods 
"""
list methods are functions that are specific to the list data type
Examples are: 
.insert()
.remove()
.append()
.index()
"""
username_list = ["elaarson", "fgarcia", "tshah", "sgilmore"]
print(username_list)

#.insert()
username_list.insert(2,"wjaffrey")
print(username_list)
#.remove()
username_list.remove("elaarson")
print(username_list)
#.append() adds input to the end of the list
username_list.append("btang")
print(username_list)
#.index()
username_index = username_list.index("tshah")
print(username_index)