# sharks intro to python


# data types
# string

a = 'this is a string'

# integer

b = 5


# functions
# functions have 2 parts, a definition, and an execution
# you need to define the function first, then you can execute the function
# functions definitions start with a def, like this; def function1():
# best way to think about functions is in 3 parts; inputs, middle, and outputs
# function best practice is to name them using snake case, that is lower case with underscores
# functions should also have a docstring that explains what they do
# they may(not necessarily) take inputs, the always do something in the middle, and they may (not neccessarily) have an output
# below is a function that takes 2 inputs, does something and has one output

def multiply_func(a, b):
    '''this is a multiline docstring. this function takes two integers 
    as inputs and multiplies them together
    '''
    output = a*b
    return output

# the inputs are a and b, the middle does the work, and out the output is 'output'
# executing a function looks like this; output = function1()
# to execute our function defined above we need to give it 2 inputs as required by the definition
# we can store the output as a new object 'answer'

answer = multiply_func(5, 9)

# you can reuse the function definition to pass different inputs, and store another output, like this

answer2 = multiply_func(4, 3)

# here is a different function that doesnt take any inputs, and doesnt return any outputs

def name_age():
    '''this function prints my name and age'''
    name = 'ben'
    age = 34
    message = name + ' is ' + str(age)
    print(message)

# here is how you execute this function, no inputs no returns required. it will just print the output

name_age()

# if you werent going to use functions you could just write code to do the same thing like this

name = 'ben'
age = 34
message = name + ' is ' + str(age)
print(message)

# but wrapping it in a function is best practice, in python you should avoid using global variables (stored objects that arent inside a function)
# the above code could be replaced with this 

def name_age():
    '''this function prints my name and age'''
    name = 'ben'
    age = 34
    message = name + ' is ' + str(age)
    print(message)

name_age()

# the above just wraps code within a function definition, and then executes that definition

# and thats the basis of functions!
