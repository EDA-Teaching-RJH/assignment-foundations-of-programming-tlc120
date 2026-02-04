def main():
    def init_database():
        Names = ["James", "William", "Worf", "Hikaru", "Data"]
        Ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
        Divisions = ["Command", "Command", "Security", "Command", "Operations"]
        IDs = ["100", "101", "102", "103", "104"]
        
        return Names, Ranks, Divisions, IDs
    
    Names, Ranks, Divisions, IDs = init_database()

    def display_menu():
        user_name = input("Please enter your full name: ")

        print(f"\n{user_name} logged in.")
        print("___ Menu____")
        print("1. Add Member")
        print("2. Remove Member")
        print("3. Update Rank")
        print("4. Display Roster")
        print("5. Search Crew")
        print("6. Filter By Division")
        print("7. Calculate Payroll")
        print("8. Count Officers")

        choice = input("Select choice: ")

    display_menu()

main()