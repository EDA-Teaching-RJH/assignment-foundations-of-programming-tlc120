def init_database():
    names = ["James T. Kirk", "William Riker", "Worf", "Hikaru Sulu", "Data"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divs = ["Command", "Command", "Security", "Sciences", "Operations"]
    ids = ["100", "101", "102", "103", "104"]
        
    return names, ranks, divs, ids


def display_menu(names, ranks, divs, ids):
    
    user_name = input("Please enter your full name: ")

    print(f"{user_name} logged in.")
    
    while True:
        print(f"\n____ Menu____")
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
            add_member(names, ranks, divs, ids)
    

        elif choice == "2":
            print("You choice is 2")
            remove_member(names, ranks, divs, ids)


        elif choice == "3":
            print("You choice is 3")  
            update_rank(names, ranks, ids) 


        elif choice == "4":
            print("You choice is 4")  
            display_roster(names, ranks, divs, ids) 


        elif choice == "5":
            print("You choice is 5")  
            search_crew(names, ranks, divs, ids)


        elif choice == "6":
            print("You choice is 6")  
            filter_by_division(names, divs)   


        elif choice == "7":
            print("You choice is 7")  
            calculate_payroll(ranks)   


        else:
            print("Invalid number")


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
                
                
def update_rank(names, ranks, ids):
    up_rank = input("Please enter the ID: ")

    if up_rank in ids:
        up_id = ids.index(up_rank)
        print(ranks[up_id], "-" ,names[up_id], "-" ,ids[up_id])
                        
        up = input("Please enter the rank you want to update: ")

        ranks[up_id] = up
                        
        print("The member's rank updates")

    else:
        print("This crew member is not exist")

                
def display_roster(names, ranks, divs, ids):
    print("The Crew member table: ")
    
    for member in range(len(names)):
        print(names[member] , "-" , ranks[member], "-" , divs[member], "-" , ids[member]) 


def search_crew(names, ranks, divs, ids):

    sea = input("Please enter a term whose name of the crew member contains that term: ")

    if sea == "James" or sea =="T" or sea == "Kirk":
        print(names[0], "-", ranks[0], "-", divs[0], "-", ids[0])

    elif sea == "William" or sea == "Riker":
        print(names[1], "-", ranks[1], "-", divs[1], "-", ids[1])

    elif sea == "Worf":
        print(names[2], "-", ranks[2], "-", divs[2], "-", ids[2])
    
    elif sea == "Hikaru" or sea =="Sulu":
        print(names[3], "-", ranks[3], "-", divs[3], "-", ids[3])

    elif sea == "Data":
        print(names[4], "-", ranks[4], "-", divs[4], "-", ids[4])
    
    else:
        sea == ""
        print("This crew member is not exist")


def filter_by_division(names, divs):
    fil = input("Please enter the division of the Crew member: ")

    if fil == "Command":
        print(names[0], "-", divs[0])
        print(names[1], "-", divs[1])


    elif fil == "Operations":
        print(names[4], "-", divs[4])
    
    elif fil == "Sciences":
        print(names[3], "-", divs[3])

    elif fil == "Security":
        print(names[2], "-", divs[2])

    else:
        fil == ""
        print("This crew member is not exist")





def calculate_payroll(ranks):
    payroll = input(f"Are you want to calculate the Credit value to ranks ? ")

    if payroll == "yes":

        Captain = 1000
        Commander = 300
        Lt_Commander = 500
        Lieutenant = 700
        calculate = [1000, 300, 500, 700, 500]

        total = Captain + Commander + Lt_Commander + Lieutenant + Lt_Commander

        for cal in range(len(ranks)):
            print(ranks[cal] ,"=", calculate[cal])
        
        print(f"The total payroll is {total}")
        



                






def main():
    names, ranks, divs, ids = init_database()
    display_menu(names, ranks, divs, ids)
main()