books = ["god killer", "goku life", "100 year truster", "world of one piece", "immortal king"]

def lib():
    while 1:
        print("\n========= Library Menu =========")
        option = int(input("1. List of the Books\n2. Find the Book\n3. Return the Book\n4. Exit\nEnter The Option: "))

        if option == 1:
            print("Collection of books")
            for book in books: print(book)
            print("\n")
            
        elif option ==2:
            want = input("Enter The Book Name : ")
            find = ""
            for book in books: 
                if want== book :
                    find = book
            if find == want:
                print(f"Your Find Book is '{find}'")
                books.remove(find)

            else:
                print("Not Available")
            
            
        elif option == 3:
            return_Book = input("Enter The Return Book Name : ")
            if return_Book == find :
                books.append(return_Book)
            print("\nCollection of books :")
            for book in books: print(book) 
            
        elif option == 4:
            print("Your Exit Application")
            exit
            
        else:
            print("Your Enter Invalid Option!")

lib()