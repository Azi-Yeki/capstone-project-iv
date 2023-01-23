#created a class called Shoe.

class Shoe:

#create a constructor method with parameters, self, country, code, product, cost, quantity.
#created the attributes
#set self to the different attributes

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

#created a method called get_cost which returns self.cost
#created another method called file_updated
#created a method called get_quantity which returns the quantity
#created a method that rethurns the string representation of the code, product, cost and quantity

    def get_cost(self):
        return self.cost

    def file_updated(self):
        return f'''{self.country},{self.code},{self.product},{self.cost},{self.quantity}'''

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f'''\nCountry:{self.country}
Shoe Code: {self.code}
Shoe Name: {self.product}
Shoe Cost: {self.cost}
Quantity: {self.quantity}\n''')

#created an open list with the variable shoe_list where all the list will be appended

shoe_list = []

#created a function called read_shoes_data.
#then also open the text file called inventory.txt and read from it
#changed its name to shoe_list_inventory
#created a variable shoe_list_inside_file
#use .readlines to read through the text file

def read_shoes_data():
    try:

        with open('inventory.txt', 'r') as shoe_list_inventory:
            shoe_list_inside_file = shoe_list_inventory.readlines()

#created a for loop
#range 1 meaning the second line in the file
#calculate using len
#strip to remove new lines
#split at the commas
#call the Shoe class
#append to the shoe list

        for line in range(1, len(shoe_list_inside_file)):
            country, code, product, cost, quantity = shoe_list_inside_file[line].strip('\n').split(',')
            shoes = Shoe(country, code, product, float(cost), int(quantity))
            shoe_list.append(shoes)

    except FileNotFoundError:
        print('inventory file not found. Please check file name correctly')

read_shoes_data()

#created a method called capture_shoes
#ppassed in parameters(shoe_country,shoe_code,shoe_name,shoe_cost,shoe_quantity)
#created an object named shoes_captured.
#append to our shoe_list.

def capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity):
    shoes_captured = Shoe(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity)
    shoe_list.append(shoes_captured)

# We create a new method.
# This is will update the quantity once.

def update():

#create a variable called object_data to take the shoe objects.

    object_data = f'Country,Code,Product,Cost,Quantity'

#created a for loop to iterate over the shoe list
#open the file and write to it

    for shoe in shoe_list:
        object_data += '\n' + shoe.file_updated()

    with open('inventory.txt', 'w') as shoe_list_inventory:
        shoe_list_inventory.write(object_data)

#created a function called view_all to print all details of the shoes
#call the print function to display the shoe_list

def view_all():
    print(*shoe_list)

#created a method called re_stock
#created a variable called qty and initialise it to the shoe_list index 0
#created a counter and initialise it to 0

def re_stock():

    qty = shoe_list[0].quantity
    shoe_index = 0

#made a for loop and use enumerate to iterate our shoe list which will allow us to iterate (shoe_list)
#return the shoe_index

    for i, s in enumerate(shoe_list):
        if s.get_quantity() < qty:
            qty = s.quantity
            shoe_index = i

    return shoe_index

#created a method called search_shoe and pass the parameter s_code
#created a for loop for our shoe_code
#created an if statement for the shoe code to call the .code and if it's equal to what the user entered, return the code and if it isn't, return a message that it isn't found

def search_shoe(s_code):

    for shoe_code in shoe_list:
        if shoe_code.code == s_code:
            return shoe_code

    return f'The shoe code {s_code} is not found\n'

#created a method called value_per_item
#created a for loop to iterate hrough the list
#calculate the total value for ech item
#print the shoe details and their total values

def value_per_item():

    for s in shoe_list:
        value = s.cost * s.quantity
        print(f'{s}Value: {value}\n')

#created a method called highest_qty() to determine the product with the highest quantity
#created a counter called shoe_index and initialise it to 0
#created a variable called max_quatity which will then take the shoe_list and the counter and call method.get_quantity
#print the shoe as being on sale
#created a for loop and use emunerate to iterate the list and keep track of the index
#created an if statement to get the shoe with the highest value
#display that the shoe is on sale

def highest_qty():
    shoe_index = 0
    max_quantity = shoe_list[shoe_index].get_quantity()

    for s, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > max_quantity:
            max_quantity = shoe.get_quantity()
            shoe_index = s

    print("This shoe is on sale: " + str(shoe_list[shoe_index]))

#created the logic
#menu to execute each function depending on the user's choice

user_choice = ''' '''

# We create a while loop, giving the user options to choose from

while user_choice != "end stock taking":
    user_choice = input("Please view below and select \n c = Capture shoe data \n vw = View all shoes \n r = Shoes that need to be restocked \n f - Find a shoe \n v = Calculate total value \n s = Shoe on sale \n Your choice: ")

#if the user enters "c", they have to enter the shoe details as prompted
#call the capture_shoes method.

    if user_choice.lower() == "c":
        shoe_country = input('Please enter the country of the shoes ')
        shoe_code = input('Please enter the shoe code ')
        shoe_name = input('Please enter product name ')
        shoe_cost = float(input('Please enter the cost of the shoe '))
        shoe_quantity = int(input('Please enter the quantity of the shoes '))
        capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity)

#when a user enters "vw, the program calls upon the view_all method

    elif user_choice.lower() == "vw":
        view_all()

#if the user enters "r", an index for the shoes is created and assigned to the re_stock() function
#display the shoe with the lowest quantity and give the option to restock or not
#if yes, they enter the quantity, if not, return to the menu
#call the methods update() and re_stock()

    elif user_choice.lower() == "r":
        shoe_index = re_stock()

        print("The shoe with the lowest quantity: " + str(shoe_list[shoe_index]))
        restock_choice = input("Restock? \n Your choice: \n Y - yes \n N - no \n")

        if restock_choice.lower() == "y":
            shoe_list[shoe_index].quantity = int(input("How many? : \n"))

        if restock_choice.lower() == "n":
            print("No restock \n")

        update()
        re_stock()

#if "f" is entered, the user inputs the code and if it's found, the sshoe is displayed. if not, it prints the code isn't found

    elif user_choice.lower() == "f":
        s_code = input("Enter the shoe code: ")

        print(f'{search_shoe(s_code)}')

#if the user enters "v", the value function is called

    elif user_choice.lower() == "v":
        value_per_item()

#if the user enters "v, the highest.qty() function is called

    elif user_choice.lower() == "s":
        highest_qty()

#if user enters "end stock taking", we exist the programme

    elif user_choice.lower() == "end stock taking":
        print("Thank you")

#if user enters an invalid option, the else statement will be executed

    else:
        print("Invalid choice. Please try again.")