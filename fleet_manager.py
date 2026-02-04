def main():
    def init_database():
        names = ["James T. Kirk", "William Riker", "Worf", "Hikaru Sulu", "Data"]
        ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
        divs = ["Command", "Command", "Security", "Command", "Operations"]
        ids = ["100", "101", "102", "103", "104"]
        
        return names, ranks, divs, ids
    
    names, ranks, divs, ids = init_database()

    def display_menu():
        user_name = input("Please enter your full name: ")

        print(f"\n{user_name} logged in.")

        while True:
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
        
        
            if choice == "1":  
                print("You choice is 1")

                def add_member(names, ranks, divs, ids):
                    
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
                
                add_member(names, ranks, divs, ids)
        
            elif choice == "2":
                print("You choice is 2")    
            
                def remove_member(names, ranks, divs, ids):

                    rem_id = input("Please enter the ID: ")

                    if rem_id in ids:
                        rem_ids = ids.index(rem_id)
                        names.pop(rem_ids)
                        ranks.pop(rem_ids)
                        divs.pop(rem_ids)
                        ids.pop(rem_ids)
                        print("The member is removed")

                    else:
                        print("This crew member is not exist")
                
                remove_member(names, ranks, divs, ids)


            else:
                print("Invalid number")

        
            
            

    display_menu()
    
main()