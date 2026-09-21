class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        print("Current waitlist:")
        current = self.head

        while current is not None:
            print(f"- {current.name}")
            current = current.next

    def add_end(self, name):
        new_node = Node(name)

        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            print(f"{name} added to the end of the waitlist")
            return

        # Find the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # Add the new node to the end
        current.next = new_node

        print(f"{name} added to the end of the waitlist")

    def remove(self, name):
        # If the list is empty
        if self.head is None:
            print(f"{name} not found")
            return

        # If the node to remove is the head
        if self.head.name == name:
            self.head = self.head.next
            print(f"Removed {name} from the waitlist")
            return

        # Search for the node
        current = self.head

        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                print(f"Removed {name} from the waitlist")
                return

            current = current.next

        # Name was not found
        print(f"{name} not found")


def waitlist_generator():
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)

        elif choice == "4":
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break

        else:
            print("Invalid option. Please choose 1–5.")


# Run the program
waitlist_generator()
