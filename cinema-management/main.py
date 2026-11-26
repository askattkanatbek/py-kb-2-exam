from halls import add_hall, show_halls
from movies import add_movie, show_movies, delete_movie



while True:
    print("1. Add Hall")
    print("2. Show Halls")
    print("3. Add Movie")
    print("4. Show Movies")
    print("5. Delete Movie")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_hall(halls)
    elif choice == "2":
        show_halls(halls)
    elif choice == "3":
        add_movie(movies)
    elif choice == "4":
        show_movies(movies)
    elif choice == "5":
        delete_movie(movies)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
