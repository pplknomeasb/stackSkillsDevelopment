def main():

    endProgram = False


    while endProgram == False:

        #Asking the user to input a desired printout and then prints it out
        userInput = input ("Please enter the string you want to be printed out: ")
        print(userInput)

        #Asking the user if they want to print another input suggestion. Changes all to uppercase for program sesitivity.
        userDecision = input ("Enter Y to do again.  Enter N to end program: ").upper()

        #Check case.  If any case isn't true...triggers the user to try again
        while userDecision != "Y" and userDecision != "N":
            userDecision = input("Sorry, you must enter Y or N. Do you want to continue printing data to the console? ").upper()


            if userDecision == "Y" or userDecision == "N":
                break

        if userDecision == "N":

            endProgram = True


if __name__ == "__main__":
    main()
    print("Goodbye!")