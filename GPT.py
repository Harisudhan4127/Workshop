import time

# Global book list
books = ["god killer", "goku life", "100 year truster", "world of one piece", "immortal king"]
borrowed_books = []

def lib():
    while True:
        print("\n========= Library Menu =========")
        option = int(input("1. List of the Books\n2. Borrow a Book\n3. Return a Book\n4. Exit\nEnter Your Option: "))

        if option == 1:
            print("\n📚 Collection of Available Books:")
            for book in books:
                print(f"- {book}")
        
        elif option == 2:
            want = input("Enter the Book Name to Borrow: ").strip().lower()
            found = False
            for book in books:
                if want == book.lower():
                    found = True
                    books.remove(book)
                    borrowed_books.append(book)
                    print(f"✅ You have borrowed '{book}'")
                    break
            if not found:
                print("❌ Book Not Available")

        elif option == 3:
            return_book = input("Enter the Book Name to Return: ").strip().lower()
            returned = False
            for book in borrowed_books:
                if return_book == book.lower():
                    borrowed_books.remove(book)
                    books.append(book)
                    returned = True
                    print(f"✅ You have returned '{book}'")
                    break
            if not returned:
                print("❌ You didn't borrow this book")

        elif option == 4:
            print("👋 Exiting Library Application...")
            time.sleep(1)
            break

        else:
            print("⚠️ Invalid Option! Please choose between 1-4.")

# Run the library system
lib()
