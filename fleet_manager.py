def main():
    def init_database():
        names = ["James", "William", "Worf", "Hikaru", "Data"]
        ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
        divs = ["Command", "Command", "Security", "Command", "Operations"]
        ids = ["100", "101", "102", "103", "104"]
        
        return names, ranks, divs, ids
    
    names, ranks, divs, ids = init_database()

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

        def add_member(names, ranks, divs, ids):
            
            if choice == "1":  
                print("You choice is 1")

                new_name = input("Name: ")
                if new_name in names:
                    print("Invalid name")
                else:
                    print("Name added")
                    names.append(new_name)
               
                new_rank = input("Rank: ")
                if new_rank in ranks:
                    print("Rank added")
                    ranks.append(new_rank)
                else:
                    print("Invalid Rank")
                    
                new_div = input("Division: ")
                if new_div in divs:
                    print("Division added")
                    divs.append(new_div)
                else:
                    print("Invalid Division")
                    
                new_ids = input("ID: ")
                if new_ids in ids:
                    print("Invalid ID")
                else:
                    print("ID is added")
                    ids.append(new_ids)
                


            else:
                print("Invalid number")

        
        add_member(names, ranks, divs, ids)

    display_menu()
    
main()


    