""" menus.py - program with a separate menu function """

def main():
    name = input("Enter your name: ")
    menu(name)
    print("Finished.")

def menu(name):
    choice = ""
    while choice.upper() != "Q":
        print("\nMenu:")
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        choice = input(">>> ")

        if choice.upper() == "H":
            print(f"Hello {name}")
        elif choice.upper() == "G":
            print(f"Goodbye {name}")
        elif choice.upper() == "Q":
            pass  # exit the loop
        else:
            print("Invalid choice")

main()
