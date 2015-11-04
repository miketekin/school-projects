'''
Author: Michael Tekin, CS115-009,
        michael.tekin@uky.edu

Assignment: Program 2

Purpose: Help the user practice adding, subtracting, multiplying, and 
dividing fractions

Preconditions: The users name, the desired difficulty level, and two numbers
#BONUS - and the number of problems they want to be given

Postconditions: Store the result of two arithmetic operations, compare with the 
users answers, and give feedback based on the comparison

Date completed: 18 October, 2015
'''

from graphics import *
from random import randrange, choice

def main():
    
    #I felt that the instructions on documentation imply that I need even more 
    #documentation than I have. However I feel that this is already a bit much
    #and any more would be redundant because most of my variable names are 
    #self-explanatory.    
    
    #In order to avoid having braces displayed by the Text() constructor
    #(including when entries are left blank), use concatenation when building 
    #string objects for Text() arguments
    
    #Set the window height and width to variables, so that graphics in the 
    #window will stay lined up if the window size is adjusted
    win_x = 600
    win_y = 600
    win = GraphWin('Fractions!', win_x, win_y)
    #Set a y-coordinate to orient the text on the first screen around, allowing
    #us to easily reposition all the text below the title if needed
    screen_1_y = 125 #upper-bound of text below the title on the first screen
    
    
    #1.0 Display the intro screen
    #1.1 Display the title of the program
    title_message = Text(Point(win_x/2, 50), 'Fraction Tutor')
    title_message.setSize(18)
    title_message.setTextColor('green')
    title_message.draw(win)
    
    #1.2 Let the user know they need to click to continue
    #Assign the x and y coordinates to variables so that we can keep the box 
    #aligned if the message is moved
    continue_message_x = win_x*(5/6)
    continue_message_y = win_y*(11/12)
    continue_message = Text(Point(continue_message_x, continue_message_y), 
                            'Click to continue')
    continue_message.draw(win)
    continue_message_box = Rectangle(Point(continue_message_x-65, 
                                           continue_message_y-15),
                                     Point(continue_message_x+65, 
                                           continue_message_y+15))
    continue_message_box.draw(win)      
    
    #1.3 Ask the user to enter their name
    name_message = Text(Point(win_x/2, screen_1_y), "What's your name?")
    name_message.setSize(14)
    name_message.draw(win)
    name_entry = Entry(Point(win_x/2, screen_1_y+30), 12)
    name_entry.draw(win)
    
    #1.4 Ask the user to enter their desired difficulty level
    difficulty_message = Text(Point(win_x/2, screen_1_y+80), 
                              'What difficulty do you want? (1-3)')
    difficulty_message.setSize(14)
    difficulty_message.draw(win)
    difficulty_entry = Entry(Point(win_x/2, screen_1_y+110), 12)
    difficulty_entry.draw(win)
    
    #BONUS#1.5 Ask the user to enter the number of problems they want to be
    #given
    rounds_message = Text(Point(win_x/2, screen_1_y+160), 
                          'How many problems do you want to do?')
    rounds_message.setSize(14)
    rounds_message.draw(win)
    rounds_entry = Entry(Point(win_x/2, screen_1_y+190), 12)
    rounds_entry.draw(win)
    
    #2. Pause the program to give the user time to fill in the entry boxes
    win.getMouse()
    
    #Assign the users entries to unique variables to be used later
    student_name = name_entry.getText()
    chosen_difficulty = difficulty_entry.getText()
    #BONUS#
    #The number of problems the user wants to be given
    chosen_rounds = rounds_entry.getText() 
    
    #If the input for difficulty is anything other than 1, 2, or 3, set
    #the difficulty to 1. This way the label for difficulty level will always 
    #be accurate.
    if chosen_difficulty.isdigit():
        if int(chosen_difficulty) > 3:
            chosen_difficulty = '1'
    else:
        chosen_difficulty = '1'
    
    
    #3.0 Go to the next screen
    #3.1 Clear the questions and entry boxes from the screen
    name_message.undraw()
    name_entry.undraw()
    difficulty_message.undraw()
    difficulty_entry.undraw()
    #BONUS#
    rounds_message.undraw()
    rounds_entry.undraw()
    
    student_label = ('Student: ' + student_name)
    student_message = Text(Point((win_x/4), win_y/6), student_label)
    student_message.setSize(12)
    student_message.draw(win)
    
    difficulty_label = ('Difficulty: ' + str(chosen_difficulty))
    difficulty_message = Text(Point(win_x*(3/4), win_y/6), difficulty_label)
    difficulty_message.setSize(12)
    difficulty_message.draw(win)
    
    
    #BONUS#
    #Use chosen_rounds to get a number that can be used in range()
    if chosen_rounds.isdigit():
        number_of_rounds = int(chosen_rounds)
    else:
        number_of_rounds = 1
        
    #BONUS#
    #Initialize a counter for the number of problems the user has gotten 
    #correct
    number_correct = 0
    #Bonus#Loop through the program
    for i in range(number_of_rounds):
    
        #4.0 Generate random numbers for our numerators and denominators
        #4.1 Make an empty list we can use to store values we get when we 
        #loop randrange. 
        numbers = []
        
        #4.2.0 For each of the 4 numbers in our fraction problem
        for i in range(4):
            #If the difficulty level is equal to '2'
            if chosen_difficulty == '2':
                #4.2.1 Add a random number to our empty list, using the level 2 
                #range
                numbers.append(randrange(6, 15))
            #If instead of the previous case the difficulty level is equal to 
            #'3'
            elif chosen_difficulty == '3':
                #4.2.2 Add a random number to our empty list, using the level 3 
                #range
                numbers.append(randrange(11, 25))
            #If the difficulty is neither '2' nor '3'
            else:
                #4.2.3 Add a random number to our empty list, using the level 1 
                #range
                numbers.append(randrange(1, 10))
    
        #4.3 Assign each number in our fraction problem to a number from the 
        #list we built - containing 4 random integers
        numerator_1 = numbers[0]
        numerator_2 = numbers[1]
        denominator_1 = numbers[2]
        denominator_2 = numbers[3]
    
    
        #5. Choose a random operator from "+-*/" to use for the problem. Assign 
        #it to a unique variable so that it can be used later.
        operator = choice('+-*/')
        
        #6. Use the randomly chosen operator to determine how the answers will 
        #be calculated. Then assign a unique variable to each answer.
        
        calculated_denominator = (denominator_1 * denominator_2)
        
        if operator == '+':
            calculated_numerator = ((numerator_1 * denominator_2) + 
                                    (denominator_1 * numerator_2))
        elif operator == '-':
            calculated_numerator = ((numerator_1 * denominator_2) - 
                                    (denominator_1 * numerator_2))
        elif operator == '*':
            calculated_numerator = (numerator_1 * numerator_2)
            
        else:
            calculated_numerator = (numerator_1 * denominator_2)
            calculated_denominator = (denominator_1 * numerator_2)
    
        
        #7. Display the problem            
        
        fraction_1_numerator = Text(Point(win_x/4, (win_y/3)-22), numerator_1)
        fraction_1_numerator.setSize(16)
        fraction_1_numerator.draw(win)
        
        fraction_1_denominator = Text(Point(win_x/4, (win_y/3)+22), 
                                      denominator_1)
        fraction_1_denominator.setSize(16)
        fraction_1_denominator.draw(win)
        
        fraction_1_division_line = Line(Point((win_x/4)-18, win_y/3),
                                       Point((win_x/4)+18, win_y/3))
        fraction_1_division_line.setWidth(2)
        fraction_1_division_line.draw(win)
        
        fraction_operator = Text(Point(win_x*(3/8), win_y/3), operator)
        fraction_operator.setSize(16)
        fraction_operator.draw(win)
        
        fraction_2_numerator = Text(Point(win_x/2, (win_y/3)-22), numerator_2)
        fraction_2_numerator.setSize(16)
        fraction_2_numerator.draw(win)
        
        fraction_2_denominator = Text(Point(win_x/2, (win_y/3)+22), 
                                      denominator_2)
        fraction_2_denominator.setSize(16)
        fraction_2_denominator.draw(win)
        
        fraction_2_division_line = Line(Point((win_x/2)-18, win_y/3),
                                       Point((win_x/2)+18, win_y/3))
        fraction_2_division_line.setWidth(2)
        fraction_2_division_line.draw(win)    
        
        fraction_equal_sign = Text(Point(win_x*(5/8), win_y/3), '=')
        fraction_equal_sign.setSize(16)
        fraction_equal_sign.draw(win)
        
        #Display the entry boxes and division line for the answer to get
        #the users answers as a numerator and a denominator
        
        numerator_entry = Entry(Point(win_x*(3/4), (win_y/3)-22), 3)
        numerator_entry.setSize(16)
        numerator_entry.draw(win)
        
        denominator_entry = Entry(Point(win_x*(3/4), (win_y/3)+22), 3)
        denominator_entry.setSize(16)
        denominator_entry.draw(win)
          
        answer_division_line = Line(Point(win_x*(3/4)-30, win_y/3), 
                                    Point(win_x*(3/4)+30, win_y/3)) 
        answer_division_line.setWidth(2)
        answer_division_line.draw(win)    
    
    
        #8. Rather than typecasting the entries to integers in order to test 
        #equality, typecast the calculated answers to strings. This will keep 
        #the program from crashing if the entry box is left blank. It will also 
        #allow us to concatenate the calculated answers with our feedback
        calculated_numerator = str(calculated_numerator)
        calculated_denominator = str(calculated_denominator)
        
    
        #9. Pause the program to give the user time to enter in their answers
        win.getMouse()
        
        user_numerator = numerator_entry.getText()
        user_denominator = denominator_entry.getText()
        
        #10.0 Determine and set the feedback to be given to the user
        #10.1 If the users answers don't match the calculated answers
        if ((user_numerator != calculated_numerator) and 
            (user_denominator != calculated_denominator)):
            #10.2 Set feedback to give the correct numerator and denominator
            #and the sad image
            feedback_text = (student_name + ', your numerator should be ' + 
                             calculated_numerator + 
                             '\n and your denominator should be ' +
                             calculated_denominator)
            feedback_image = 'sad.gif'
            
        #If instead of the previous case only the numerators match
        elif ((user_numerator == calculated_numerator) and 
              (user_denominator != calculated_denominator)):
            #10.3 Set feedback to give the correct denominator and the sad 
            #image
            feedback_text = (student_name + ', your denominator should be ' +
                             calculated_denominator)
            feedback_image = 'sad.gif'

        #If instead of the previous cases only the denominators match
        elif (user_denominator == calculated_denominator) and (
              user_numerator != calculated_numerator):
            #10.4 Set feedback to incorrect-numerator text and the sad image
            feedback_text = (student_name + ', your numerator should be ' + 
                             calculated_numerator)
            feedback_image = 'sad.gif'
        
        #If neither of the users inputs were incorrect
        else:
            feedback_text = ("You're right!! " + student_name)
            feedback_image = 'happy.gif'
            
            #BONUS#
            number_correct += 1
            
        
        #Display the feedback
        feedback_message_image = Image(Point(win_x/2, win_y*(2/3)-25), 
                                       feedback_image)
        feedback_message_image.draw(win)
        feedback_message_text = Text(Point(win_x/2, 500), feedback_text)
        feedback_message_text.setSize(14)
        feedback_message_text.draw(win)
        
        #BONUS#Pause the program to give the user time to view their feedback
        win.getMouse()
        #Bonus#Clear the screen, to give space to either the next problem or
        #to the results
        feedback_message_text.undraw()
        feedback_message_image.undraw()
        fraction_1_numerator.undraw()
        fraction_1_denominator.undraw()
        fraction_1_division_line.undraw()
        fraction_operator.undraw()
        fraction_2_numerator.undraw()
        fraction_2_denominator.undraw()
        fraction_2_division_line.undraw()
        fraction_equal_sign.undraw()
        numerator_entry.undraw()
        denominator_entry.undraw()
        answer_division_line.undraw()
    #End of for loop    
    
    
    #BONUS#Tell the user how many problems they got correct out of the total
    number_correct_text = ('You got ' + str(number_correct) + ' out of ' + 
                           str(number_of_rounds) + ' problems correct.')
    number_correct_message = Text(Point(win_x/2, win_y/3), 
                                  number_correct_text)
    number_correct_message.setSize(14)
    number_correct_message.setTextColor('green')
    number_correct_message.draw(win)
    continue_message.setText('Click to exit')
    
    
    #11. Pause the program in order to let the user quit out when they're ready
    win.getMouse()
    
    #12. Quit the program
    win.close()
    
    
main()
