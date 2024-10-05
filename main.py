import random

print("PASSWORD GENERATOR")
numberofcharacters = input("Enter how many charcters: ")

while not numberofcharacters.isnumeric():
    print("Invalid input, please enter a number")
    numberofcharacters = input("Enter how many charcters: ")
    

numberofcharacters = int(numberofcharacters)
if numberofcharacters > 69:
    print("Limit of characters is 69\nGenerating 69 character password")
    numberofcharacters = 69

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '*', '+']
def genpassword(length):
    global password
    password = random.sample(characters,length)
    random.shuffle(password)
    password = ''.join([str(elem) for elem in password])
    return password

genpassword(numberofcharacters)
print("YOUR PASSWORD IS:")
print(password)

#print(len(characters))