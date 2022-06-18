#Author: Michael Tekin, CS115-009,
#        michael.tekin@uky.edu
#Assignment: Program 1
#Purpose: Generate and provide the user with a hashed code
#Preconditions: For each prompt obtain input from the user
#Postconditions: Generate a hash and display it to the user along with their
#                their name and id
#Date completed: 9-27-15

from hashlib import sha256

def main():

    #1. For each input given by the user and for each computation,
    #   initialize a unique variable, in order to later manipulate those values
    
    #2. Prompt the user to enter their first name
    name_first = input('Enter your first name: ')
    
    #3. Prompt the user to enter their last name
    name_last = input('Enter your last name: ')
    
    #4. Prompt the user to enter a userid (similar to the ones we use at UK)
    user_id = input('Enter your userid: ')
    
    #5. Prompt the user to enter a password
    user_password = input('Enter your password: ')
    
    #6. Append the userid to the end of the password
    password_and_salt = user_password + user_id
    
    #7. Hash the concatenated password and userid
    hashed_password = sha256(password_and_salt.encode()).hexdigest()
    
    #8. Display the userid, full name and hashed password on the screen, 
    #   separated by colons
    print()
    print(user_id + ':' + name_first + ' ' + name_last + ':' + hashed_password)
    
    #BONUS
    #Get a password from the user to check against the first password
    user_password_again = input('Enter your password again: ')
    
    #Append the userid to the password in question
    password_and_salt_again = user_password_again + user_id
    
    #Hash the concatenated password in question and userid
    hashed_password_again = sha256(password_and_salt_again.encode()).hexdigest()
    
    #Check to see if the newly hashed password matches the first hashed password
    if hashed_password_again == hashed_password:
        print('Welcome back')
    else:
        print('You are banned')

main()
