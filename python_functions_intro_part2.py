# sharks intro to python part2


# a benefit of functions is that you can pass outputs from one function as inputs to another

def years_old(year_born, current_year):
    '''returns the age_in_years from the arguments provided, year_born and current_year'''
    age_in_years = current_year - year_born
    return age_in_years


def welcome_message(name, age):
    '''writes a welcome message using a name provided as an argument
    name must be entered as a string'''
    message = "Hi, I'm " + name + " and I'm " + str(age) + ' years old'
    return message


persons_age = years_old(1986, 2020)
message_output = welcome_message('Ben', persons_age)
print(message_output)



# defining and executing functions is better practice that just writing code line by line for various reasons.
# functions are reusable, even from external python scripts
# also make things much easier for debugging when things get complicated
# to make this code even more aligned with best practice, we should execute the functions from inside another function called 'main'
# its also clearer when you define the variables separately, like this:

def years_old(year_born, current_year):
    '''returns the age_in_years from the arguments provided, year_born and current_year'''
    age_in_years = current_year - year_born
    return age_in_years


def welcome_message(name, age):
    '''writes a welcome message using a name provided as an argument
    name must be entered as a string'''
    message = "Hi, I'm " + name + " and I'm " + str(age) + ' years old'
    return message


def main():
    '''this is the main function that defines the variables required, and brings 
    everything together to run the program'''
    year_born = 1986
    current_year = 2020
    name = 'Ben'
    
    persons_age = years_old(year_born, current_year)
    message_output = welcome_message(name, persons_age)
    print(message_output)

    
if __name__ == '__main__':
    main()

    
# with the above it makes it easier to identify that there are only 3 variables that the program uses
# def main(): is always the last function to be defined, and it brings together the execution of all the other functions
# if __name__ == '__main__': is a quirky thing, but it is best practice to use
# it allows the functions defined in the code to be called and executed in external workbooks, without executing the rest of the code in the workbook
# in conclusion the structure of a python script should be, in this order: 
# imports (if any), defining functions, defining main():, executing main():
