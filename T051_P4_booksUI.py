# T051
# Date: 12/04/2022
# Version: 1.0
# Active members
# Leena Ford 101229281 
# Isabella Fotia 101228368 
# Umayer Joarder 101227396 
# Espen Swift 101232582 

#imports
from T051_P2_add_remove_search_dataset import get_all_categories_for_book_title, get_books_by_title, get_books_by_rate, get_books_by_author, get_books_by_publisher, get_books_by_rate, get_books_by_category, add_book, remove_book
from T051_P3_sorting_fun import dictionary_to_list, sort_books_author, sort_books_publisher, sort_books_title, sort_books_ascending_rate
from T051_P5_load_data import book_category_dictionary

#constant
list_data = dictionary_to_list(book_category_dictionary("google_books_dataset.csv"))

#Function definitions for the user interface

#Function author: Leena Ford (101229281)
def display_menu()->str:
    
    """
    Preconditions: The function does not take any arguments
    Displays the menu of the user interface.
    
    >>> display_menu()
    The available commands are:
        1 - L)oad data
       2 - A)dd book
       3 - R)emove book
       4 - G)et books
            T)itle R)ate  A)uthor  P)ublisher  C)ategory
       5 - GCT) Get all categories for book Title
       6 - S)ort books
 	    T)itle  R)ate  P)ublisher  A)uthor
       7- Q)uit

    Please type your command:
    
    """
    
    
    menu = print('The available commands are:\n', '  1 - L)oad data\n', '  2 - A)dd book\n', '  3 - R)emove book\n', '  4 - G)et books\n', '\tT)itle R)ate  A)uthor  P)ublisher  C)ategory\n', '  5 - GCT) Get all categories for book Title\n', '  6 - S)ort books\n', '\tT)itle  R)ate  P)ublisher  A)uthor\n', '  7- Q)uit\n')
    
    return menu

#Function author: Leena Ford (101229281)
#Author of commands get_books_by_publisher: Umayer Joarder (101227396)
#Author of commands get_books_by_title/rate/author: Leena Ford (101229281)
def get_functions()->None:
    
    """
    Preconditions: The function takes no arguments. This function calls all the get functions, so ensure you import all necessary get-functions
    and save it in the same folder as the folder containing this function.
    
    Promps the user to enter a subcommand for the 'G' or 'g' main command in the user interface. Then calls any of the imported get-functions
    based on the user's input.
    
    >>> get_functions()
    How would you like to get books? Enter 'T', 'R', 'A', 'P' or 'C': T   [user inputs 'T']
    Enter The book title you are looking for: [user inputs 'Antiques Chop']
    ----
    The book has been found
    True
    
    >>> get_functions()
    How would you like to get books? Enter 'T', 'R', 'A', 'P' or 'C': T   [user inputs 'a']
    Enter the author you are looking for:    [user inputs 'Barbara Allan']
    ----
    The author Barbara Allan has published the following books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery, rate: 3.3
    Book 2: Antiques Con, rate: 4.8
    Book 3: Antiques Chop, rate: 4.5
    Book 4: Antiques Knock-Off, rate: 4.3
    4
    """
    
    
    get_commands = {'T': 'Enter The book title you are looking for: ', 't': 'Enter The book title you are looking for: ', 'A': 'Enter the author you are looking for: ', 'a': 'Enter the author you are looking for: ', 'P': 'Enter the publisher you are looking for: ', 'p': 'Enter the publisher you are looking for: ', 'C':'Enter the category you are looking for: ', 'c':'Enter the category you are looking for: ', 'R':'Enter an integer from 1 to 5: ', 'r':'Enter an integer from 1 to 5: '}
    
    next_line = str(input("How would you like to get books? Enter 'T', 'R', 'A', 'P' or 'C': "))

    for k in get_commands:
        if next_line == k:
            phrase = input(get_commands.get(k))
            
            if k == 'T' or k == 't':
                print(get_books_by_title(book_category_dictionary("google_books_dataset.csv"), phrase))
            elif k == 'A' or k == 'a':
                print(get_books_by_author(book_category_dictionary("google_books_dataset.csv"), phrase))
            elif k == 'P' or k == 'p':
                print(get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"), phrase))
            elif k == 'C' or k == 'c':
                category_call = print(get_books_by_category(book_category_dictionary("google_books_dataset.csv"), phrase))
            elif k == 'R' or k == 'r':
                print(get_books_by_rate(book_category_dictionary("google_books_dataset.csv"), int(phrase)))                               
   
    if next_line not in get_commands:
        print("\nSubcommand does not exist\n")
    
    return

#Function author: Leena Ford (101229281)
#Author of commands sort_books_title/ascending_rate/publisher/category: Espen Swift (101232582) 
def sort_functions()->None:
    
    """
    Preconditions: The function takes no arguments. This function calls all the sort functions, so ensure you import all necessary sorting-functions
    and save it in the same folder as the folder containing this function.
    
    
    Promps the user to enter a subcommand for the 'S' or 's' main command in the user interface. Then calls any of the imported sort-functions
    based on the user's input.
    
    >>> sort_functions()
    How would you like to sort books? Enter 'T', 'R', 'A' or 'P': [user inputs 'r']
    ----
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': ['Economics', 'Business'], 'language': 'English'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': ['Economics', 'Management'], 'language': 'English'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': ['Economics'], 'language': 'English'}....]
    
    >>> sort_functions()
    How would you like to sort books? Enter 'T', 'R', 'A' or 'P': [user inputs 'a']
    ----
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': ['Economics', 'Business'], 'language': 'English'}...]
    """
    
    sort_commands = ['T', 't', 'A', 'a', 'P', 'p', 'R', 'r']
    
    sub_line = str(input("How would you like to sort books? Enter 'T', 'R', 'A' or 'P': "))
    
    if sub_line == sort_commands[0] or sub_line == sort_commands[1]:
        print(sort_books_title(list_data))
    elif sub_line == sort_commands[2] or sub_line == sort_commands[3]:
        print(sort_books_author(list_data))
    elif sub_line == sort_commands[4] or sub_line == sort_commands[5]:
        print(sort_books_publisher(list_data))
    elif sub_line == sort_commands[6] or sub_line == sort_commands[7]:
        print(sort_books_ascending_rate(list_data))     
    else:
        print('\nsubcommand does not exist\n')
    
    
    return


#Function author: Leena Ford (101229281)
#Author of commands add_book: Isabella Fotia (101228368) 
def adding()->None:
    """
    Preconditions: The function takes no arguments. This function calls all the adding book functions, so ensure you import the add_book function
    and save it in the same folder as the folder containing this function. Make sure the category is a real category in the dataset
    
    Promps the user to enter all data for a book, and stores this as a tuple. Then calls the add_book function and stores the book data as one of the
    function parameters. If the category of the book does not exist in the dataset, then the function does not add the book, and displays this error message.
    
    >>> adding()
    Enter book title: [user inputs 'Random book title']
    Enter book author: [use inputs 'Random author']
    Enter book language: [user inputs 'English']
    Enter book publisher: [user inputs 'Random publisher']
    Enter book category: [user inputs 'Fiction']
    Enter book rate: [user inputs '3.2']
    Enter book pages: [user inputs '112']
    -------
    The book has been added correctly
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan'...}, {'title': "Random book title", 'author': 'Random author', 'rating': 3.2, 'publisher': 'Random publisher', 'pages': 112, 'category': 'Fiction', 'language': 'English'}
    
    >>> adding()
    Enter book title: [user inputs 'Random book title']
    Enter book author: [use inputs 'Random author']
    Enter book language: [user inputs 'English']
    Enter book publisher: [user inputs 'Random publisher']
    Enter book category: [user inputs 'Non-existing category in dataset']
    Enter book rate: [user inputs '3.2']
    Enter book pages: [user inputs '112']
    -----
    There was an error adding the book
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan'...}]
    """
    
    book = []
    
    titles = input('Enter book title: ')
    authors = input('Enter book author: ')
    language = input('Enter book language: ')
    publisher = input('Enter book publisher: ')
    category = input('Enter book category: ')
    rate = input('Enter book rate: ')
    pages = input('Enter book pages: ')    
    
    book += [titles,authors,language,publisher,category,rate,pages]
    
    books = tuple(book)
    print(add_book(book_category_dictionary('google_books_dataset.csv'), books))    
    
    return

#Function author: Leena Ford (101229281)
#Author of commands remove_book: Isabella Fotia (101228368)
def removing()->None:
    """
    Preconditions: The function takes no arguments. This function calls all the removing book functions, so ensure you import the remove_book function
    and save it in the same folder as the folder containing this function. Make sure the book title and category are actually present in the dataset.
    
    Promps the user to enter the book title and category of a book. Then calls the remove_book function and removes the book. If the title and category
    do not exist in the dataset, function does not remove book.
    
    
    >>> removing()
    Enter the book title you want to remove: [user inputs 'Antiques Chop']
    Enter the category of the book: [user inputs 'Fiction']
    ----
    The book has been removed correctly
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.'...}]}
    
    >>> removing()
    Enter the book title you want to remove: [user inputs 'non existing title']
    Enter the category of the book: [user inputs 'Non existing category in dataset']
    ---
    There was an error removing the book. Book not found.
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kens...}]}

    """

    
    book = []
    
    titl = input('Enter the book title you want to remove: ')
    cat = input('Enter the category of the book: ')
    
    print(remove_book(book_category_dictionary('google_books_dataset.csv'), titl, cat))    
    
    return

#Function author: Leena Ford (101229281)
#Author of commands get_all_categories_for_book_title: Umayer Joarder (101227396)

def after_loading()->None:
    """
    Preconditions: The function takes no arguments. 
    
    Calls the display menu and re-displays the commands. Depending on the user's input, this function calls the sort_functions, removing, adding or get_functions 
    written above. Otherwise, if those functions aren't necessary to call, then this function returns the appropriate output to the user's input.
    
    
    >>> after_loading()
    The available commands are:
        1 - L)oad data
        2 - A)dd book
        3 - R)emove book
        4 - G)et books
             T)itle R)ate  A)uthor  P)ublisher  C)ategory
        5 - GCT) Get all categories for book Title
        6 - S)ort books
 	     T)itle  R)ate  P)ublisher  A)uthor
        7- Q)uit
        
    Please type your command: [user inputs 'L']
    ----
    You have already loaded the data
    
    The available commands are:
        1 - L)oad data
        2 - A)dd book
        3 - R)emove book
        4 - G)et books
             T)itle R)ate  A)uthor  P)ublisher  C)ategory
        5 - GCT) Get all categories for book Title
        6 - S)ort books
 	     T)itle  R)ate  P)ublisher  A)uthor
        7- Q)uit
        
    Please type your command:
    
    >>> after_loading()
    The available commands are:
        1 - L)oad data
        2 - A)dd book
        3 - R)emove book
        4 - G)et books
             T)itle R)ate  A)uthor  P)ublisher  C)ategory
        5 - GCT) Get all categories for book Title
        6 - S)ort books
 	     T)itle  R)ate  P)ublisher  A)uthor
        7- Q)uit
        
    Please type your command: [user inputs 'GCT']
    ----
    Type the book title you want to find all the categories for: [user inputs 'Antiques Chop']
    The book title " Antiques Chop " belongs to the following categories:
    Category 1 : Fiction
    Category 2 : Detective
    Category 3 : Mystery
    
    The available commands are:
        1 - L)oad data
        2 - A)dd book
        3 - R)emove book
        4 - G)et books
             T)itle R)ate  A)uthor  P)ublisher  C)ategory
        5 - GCT) Get all categories for book Title
        6 - S)ort books
 	     T)itle  R)ate  P)ublisher  A)uthor
        7- Q)uit
        
    Please type your command: 
        
    """

    user_input = ''
    while (user_input != 'Q') and (user_input != 'q'):
        display_menu()
    
        user_input = str(input("Please type your command: "))
        
        if (user_input == 'G') or (user_input == 'g'):
            call_get = get_functions()
    
        elif (user_input == 'A') or (user_input == 'a'): 
            calling_add = adding()
            
        
        elif (user_input == 'R') or (user_input == 'r'):
            calling_remove = removing()
        
        elif (user_input == 'GCT') or (user_input == 'gct'):
            cat_title = input('Type the book title you want to find all the categories for: ')
            get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"), cat_title)
        
        elif (user_input == 'S') or (user_input == 's'):
            sort_call = sort_functions()
            
            
        elif (user_input == 'Q') or (user_input == 'q'):
            print("\nPress Q or q again to confirm you want to quit the program\n")
            return
       
        elif (user_input == 'L') or (user_input == 'l'):
            print("\nYou have already loaded the data\n")       #if the user already loaded the data       
        
        else:
            print("\nNo such command\n")
        
    
    
    return
      
#Function author: Leena Ford (101229281)

def if_loaded() -> bool:
    
    """
    Preconditions: The function does not take in any arguments. The dataset to load is the google_books_dataset.csv
    
    Determines whether the data has been loaded prior to any other command. If not, function displays this information. If the data has been loaded,
    then the after_loading function gets called.
    
    >>> if_loaded()
    The available commands are:
        1 - L)oad data
        2 - A)dd book
        3 - R)emove book
        4 - G)et books
             T)itle R)ate  A)uthor  P)ublisher  C)ategory
        5 - GCT) Get all categories for book Title
        6 - S)ort books
 	     T)itle  R)ate  P)ublisher  A)uthor
        7- Q)uit
        
    Please type your command: [user inputs 'h']
    ---
    No such command
    
    The available commands are:
        1 - L)oad data
        2 - A)dd book
        3 - R)emove book
        4 - G)et books
             T)itle R)ate  A)uthor  P)ublisher  C)ategory
        5 - GCT) Get all categories for book Title
        6 - S)ort books
 	     T)itle  R)ate  P)ublisher  A)uthor
        7- Q)uit
        
    Please type your command: 
    
    >>> if_loaded()
    The available commands are:
        1 - L)oad data
        2 - A)dd book
        3 - R)emove book
        4 - G)et books
             T)itle R)ate  A)uthor  P)ublisher  C)ategory
        5 - GCT) Get all categories for book Title
        6 - S)ort books
 	     T)itle  R)ate  P)ublisher  A)uthor
        7- Q)uit
        
    Please type your command: [user inputs 'g']
    ----
    File not loaded, please use the load command first
    
     The available commands are:
        1 - L)oad data
        2 - A)dd book
        3 - R)emove book
        4 - G)et books
             T)itle R)ate  A)uthor  P)ublisher  C)ategory
        5 - GCT) Get all categories for book Title
        6 - S)ort books
 	     T)itle  R)ate  P)ublisher  A)uthor
        7- Q)uit
    
    Please type your command:
    """
    
    display_menu()
    user_input = ''
    loaded = False
    
    while user_input != 'Q':
    
        user_input = str(input("Please type your command: "))
        
        if (user_input == 'L') or (user_input == 'l'):
            filename = input("Enter the name of the file to be loaded: ")
            print(book_category_dictionary(filename))
            loaded = True
            
            next_part = after_loading()
          
        elif (user_input == 'Q') or (user_input == 'q'):
            print("You have quit the program")
            return 
    
        elif (loaded == False):
            if (user_input == 'A') or (user_input == 'R') or (user_input == 'G') or (user_input == 'GCT') or (user_input == 'S') or (user_input == 'a') or (user_input == 'r') or (user_input == 'g') or (user_input == 'gct') or (user_input == 's'):
                print("\nFile not loaded, please use the load command first\n")
                display_menu()
                #if the user enters an existing command but before the Load command
   
            else:
                print("\nNo such command\n")
                display_menu()
              
    
    return


#Main script
if __name__ == '__main__':
    call = if_loaded()


