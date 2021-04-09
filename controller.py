import model #imports model.py
import view #imports view.py
import chart #imports chart.py
import time #imports time library

def start(): #main function to run the program
    while True: #loop condition to run program until false
        view.start_View() #runs start_View() function from view.py
        user_input = input("Enter your response: ") #gets user_input from the user
        if user_input == "1":
            print("==============HERE ARE THE RESULTS==============\n")
            view.view_all() #runs view_all() function from view.py
            print("GOING BACK TO MAIN MENU")
            time.sleep(3) #delays the next loop for 3 seconds
        elif user_input == "2":
            print("You will now be creating a new entry! \n")
            model.create_person()  #runs create_person() function from model.py
            time.sleep(2) #delays the next loop for 2 seconds
            print("===============INSERTING TO DATABASE SUCCESSFULL==============")
            print("GOING BACK TO MAIN MENU")
            time.sleep(3) #delays the next loop for 3 seconds
        elif user_input == "3":
            check_id = input("Please enter the ID you want to search for: ") #gets the check_id from the user
            print("===============SEARCHING ID... PLEASE WAIT================\n")
            time.sleep(3) #delays the next loop for 3 seconds
            print("RESULTS:")
            view.view_searchedID(check_id) #runs the view_searchedID function and takes in the check_id input from the user as a parameter
            print("GOING BACK TO MAIN MENU")
            time.sleep(4) #delays the next loop for 4 seconds
        elif user_input == "4":
            check_keyword = input("Please enter the name you want to search for: ")
            print("===============SEARCHING KEYWORD... PLEASE WAIT================\n")
            time.sleep(3) #delays the next loop for 3 seconds
            print("RESULTS:")
            view.view_searchedbykeyword(check_keyword) #runs the searchedbykeyword function and takes in the check_keyword as a parameter
            print("GOING BACK TO MAIN MENU")
            time.sleep(4) #delays the next loop for 4 seconds
        elif user_input == "5":
            check_id = input("Please enter the ID for the entry you want to delete: ") #gets the check_id from the user
            view.view_del_entry(check_id) #runs the view_del_entry function and takes in the check_id input from the user as a parameter
            time.sleep(3) #delays the next loop for 3 seconds
            print("Entry deleted!")
            print("GOING BACK TO MAIN MENU")
            time.sleep(3) #delays the next loop for 3 seconds
        elif user_input == "6":
            chart.plot_myPlot() #runs the plot_myPlot function to create an object from chart.py
            chart.plt.show() #runs the plt.show from the chart.py
        elif user_input == "exit":    
            view.end_View() #runs the end_View function to print the end_program output
            break #ends the while loop
        

if __name__ == "__main__":
    start() #run the start function
