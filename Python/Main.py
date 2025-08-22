from Services import LibraryService

def main():
    service = LibraryService()
    try :
        while True:
            print("\nLibrary Menu:")
            print("1. Register Reader")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. List Borrowed Books")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                service.register_reader()
            elif choice == "2":
                service.borrow_book()
            elif choice == "3":
                service.return_book()
            elif choice == "4":
                service.list_borrowed_books()
            elif choice == "5":
                service.close_service()
                break
            else:
                print("Invalid choice. Try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
if __name__ == "__main__":
    main()