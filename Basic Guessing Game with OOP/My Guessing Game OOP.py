"""
Basic OOP in Python for a guess the number game

Similar to https://github.com/chenmingxue/Python_PracticeProjects/blob/master/11_GuessNumber.py

"""
import random

#class declaration
class Guessnumber(object):
    def __init__(self, guessrange = 50):
        self.mystery_number = random.randint(1,guessrange)
        #generating random number from a user defined range

    def checknum(self, input_num = 0):
        #checking the number
        if input_num == self.mystery_number:
            return "Correct!"
        elif input_num > self.mystery_number:
            return "Too big"
        else:
            return "Too small"

    def shownum(self):
        #to display the generated number if player loses
        return self.mystery_number


if __name__ == "__main__":
    tries = 3 #number of tries player has to guess
    replay = True #incase user wants to play again after the first round
    num = True
    
    
    while replay:
        while tries > 0:
            while num:
                #Asking player for the guessing range and checking its validity
                guessrange = int(input("Choose a number for the upper limit of your guessing range, which should be greater than 1.\n"))
                if guessrange > 1:
                    print(f"Chosen range for the game is (1, {guessrange})")
                    guess_obj = Guessnumber(guessrange)
                    num = False
                    break
                else:
                    print("Invalid choice")

            #Asking player to guess number and checking it against the generated number
            input_num = int(input("Enter your guess.\n"))
            answer = guess_obj.checknum(input_num)
            if answer == "Correct!":
                print(f"You got it right!")
                break
            else:
                tries -= 1
                print(f"The number is {answer}")
                print(f"You have {tries} tries left")

        else:
            if tries > 0:
                print("You won!")
            else:
                print("You lose")
                print(f"The number was {guess_obj.shownum()}")

        #Checking is player is ready to play another round
        question = input("Would you like to play again? (Yes/No)\n")
        if question.lower() == "yes":
            print("Let's start over then")
            tries = 3
            num = True
        else:
            print("Okay, see you soon!")
            replay = False


                

                
                
            
