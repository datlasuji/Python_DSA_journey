print("day 2 :30 day python")

# Declaring variables
first_name = "Suji"
last_name = "Varma"
full_name = "Suji Varma"
country = "India"
city = "Vijayawada"
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True

# Declaring multiple variables in one line
x, y, z = 1, 2, 3

#data type opf python
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))


print("Length of first name:", len(first_name)) #length of fist name


#comapre the name which lenght is big
print("First name length:", len(first_name))
print("Last name length:", len(last_name))
print("Is first name longer than last name?",
      len(first_name) > len(last_name))



#number operation

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two


print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)



# area of circle
radius = 30
pi = 3.14159 
area_of_circle = pi* radius ** 2.       #1
circum_of_circle = 2 * pi * radius

print("Area of circle:", area_of_circle) #2
print("Circumference of circle:", circum_of_circle)


radius = float(input("enter radius:"))
area = 3.14 * radius * radius
print("Area of the circle is:", area )



first_name = input("enter your first name")
last_name = input("enter you last name")
country = input("enter your country")
age = input("enter your age")

print("user deatils")
print(first_name, last_name,country,age)
