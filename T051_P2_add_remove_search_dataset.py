# T051
# Date: 12/04/2022
# Version: 1.0
# Active members
# Leena Ford 101229281 
# Isabella Fotia 101228368 
# Umayer Joarder 101227396 
# Espen Swift 101232582 

#imports
from T051_P5_load_data import book_category_dictionary

#The eight functions from P2 - Task 1

#Function 1 - add_book (Written by Isabella Fotia 101228368)

    
def add_book(dictionary: dict, new_book: tuple) -> dict:
    """
        Returns the case 1 dictionary where a new book has been added at the end of the list in a particular category. It is a tuple and has seven values containing the title, author, language, publisher, category, rating, and pages. It adds the book to the dictionary and prints a message verifing that the book has been added or if it has not been added. 
        Preconditions: Make sure the category is capitalized and written correctly. Make sure the T051_P1_load_data.py file is in the same folder as this file.
        
        >>> add_book(book_category_dictionary('google_books_dataset.csv'), ('My Title', 'Isabella', 'English', 'Fotiainc', 'Fiction', '2.5', '18'))
        The book has been added correctly
        {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}...{'title': 'My Title', 'author': 'Isabella', 'language': 'English', 'publisher': 'Fotiainc', 'category': 'Fiction', 'rating': '2.5', 'pages': '18'}], 'Comics': [{'title'...}]}
        
        >>> add_book(book_category_dictionary('google_books_dataset.csv'), ('House applications', 'Myname', 'English', 'webinc', 'non-existent category', '4.2', '100'))
        There was an error adding the book
        {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English'}...}]}  
    """    
   
   
    new_dictionary = dict(dictionary)
    
    set_categ = set()
    
    for lst in new_dictionary.values():

        for d in lst:
            avail_category = d.get('category')
            values = d.values()
             
        if new_book[4] == avail_category:
            lst.append({'title' : new_book[0], 'author': new_book[1], 'language': new_book[2], 'publisher' : new_book[3], 'category' : new_book[4], 'rating' : new_book[5], 'pages' : new_book[6]})    
            
            set_categ.add(new_book[4])
            print("The book has been added correctly")
   
    if new_book[4] not in set_categ:
        print("There was an error adding the book")
            
   
    return new_dictionary    
    
   
#Function 2 - remove_book (Written by Isabella Fotia 101228368) 

def remove_book(dictionary:dict, title:str, cat_key:str) -> bool:
    """
    Returns the case 1 dictionary after it removes a book using the title and the cateogry. Then after the book has been removed it will return an updated function dictionary and prints the statements depending if the book has been removed correctly or has not been removed sucessfully.                                                                           
    Preconditions: Must type the book title and category correctly, otherwise won't recognize it. Make sure the T051_P1_load_data.py file is in the same folder as this file.
    
    >>> remove_book(book_category_dictionary('google_books_dataset.csv'), "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Fiction')
    The book has been removed correctly
    {'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}...}]}

    
    >>> remove_book(book_category_dictionary('google_books_dataset.csv'), "Imaginary Title", 'Imaginary category')
    There was an error removing the book. Book not found.
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English'}...}]}

   
    """    

    category_of_book = []
    listofbook = []
    
    dictcopy = dictionary
    
    for book in dictcopy.values():

        for d in book:
            books = d.get('title')
            categories = d.get('category')
    
            if (title == books) and (cat_key == categories):
                listofbook.append(title)
                category_of_book.append(cat_key)
                book.remove(d)
                print('The book has been removed correctly')
     
   
    if (title not in listofbook) or (cat_key not in category_of_book) or ((title not in listofbook) and (cat_key not in category_of_book)) :
            print('There was an error removing the book. Book not found.')
            
   
    return dictcopy  


     
#Function 3 - get_books_by_category (Written by Umayer Joarder 101227396) 

def get_books_by_category(imprt: dict, category: str) -> str:
    """ 
    The function returns the amount of books at the end as a string and the names of books in a certain category.
    The function takes in two input parameters imprt and category. imprt is the dictionary
    from the case1 file, we imported the function definition from the case1 file along with the
    dataset file here. Category is the category of the book which will return the information for.
    Preconditions: Make sure the category is written correctly. The imprt argument is the dictionary from
    case 1 with the function call: 'book_category_dictionary('google_books_dataset.csv')'.
    
    
    >>>get_books_by_category(book_category_dictionary('google_books_dataset.csv'), "Economics")
    The category of book- Economics ,has 22 books. The list of the books are:
    Book1:How To Win Friends and Influence People by Dale Carnegie
    Book2:Marketing (The Brian Tracy Success Library) by Brian Tracy
    Book3:Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2 by Brian Tracy
    Book4:The Power of Habit: Why We Do What We Do in Life and Business by Charles Duhigg
    Book5:Management (The Brian Tracy Success Library) by Brian Tracy
    Book6:Getting Things Done: The Art of Stress-Free Productivity by David Allen
    Book8:Rework by Jason Fried
    Book9:The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book10:Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth by T. Harv Eker
    Book11:Business Strategy (The Brian Tracy Success Library) by Brian Tracy
    Book12:Principles: Life and Work by Ray Dalio
    Book13:The Magic of Thinking Big by David J. Schwartz
    Book14:Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book15:Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk by Michael Sincere
    Book16:Predictably Irrational: The Hidden Forces that Shape Our Decisions by Dan Ariely
    Book17:Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3 by Brian Tracy
    Book18:Summary: Think and Grow Rich by Nine99 Innovation Lab
    Book19:Personal Success (The Brian Tracy Success Library) by Brian Tracy
    Book20:The Essentials of Finance and Accounting for Nonfinancial Managers by Edward Fields
    Book21:Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports by Thomas Ittelson
    Book22:Platform: Get Noticed in a Noisy World by Michael Hyatt
    22

    >>>get_books_by_category(book_category_dictionary('google_books_dataset.csv'), "Investing")
    The category of book- Investing ,has 1 books. The list of the books are:
    Book1:The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    1

    >>>get_books_by_category(book_category_dictionary('google_books_dataset.csv'), "Adventure")
    The category of book- Adventure ,has 7 books. The list of the books are:
    Book1:Sword of Destiny: Witcher 2: Tales of the Witcher by Andrzej Sapkowski
    Book2:A Feast for Crows (A Song of Ice and Fire. Book 4) by George R.R. Martin
    Book3:After Anna by Alex Lake
    Book4:The Way Of Shadows: Book 1 of the Night Angel by Brent Weeks
    Book5:A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire) by George R.R. Martin
    Book6:Edgedancer: From the Stormlight Archive by Brandon Sanderson
    Book7:The Malady and Other Stories: An Andrzej Sapkowski Sampler by Andrzej Sapkowski
    7
    
    """
    num1 = 0
    num2 = 0
    catg_lst = []
    
    for x1 in imprt: 
        
        if category == x1:   
            catg_lst = imprt.get(category)
            
    for x2 in range(len(catg_lst)):
        imprt_lst = catg_lst[x2]
        num1+=1
    
    print("\nThe category " , category , "has", num1, "books.", "This is the list of books:")
    for x3 in range(len(catg_lst)): 
        num2+=1
        shell = ("Book"+ str(num2) +":" + catg_lst[x3].get("title") + " by " + catg_lst[x3].get("author"))
        print(shell) 
    print("Number of books in this category:")
    
    return num2


#Function 4 - get_books_by_rate (Written by Espen Swift 101232582)


def get_books_by_rate(input_dict: dict, rate: int)->str:
    """
    Returns the number of books in a given rate and lists them out by title and author.
    Preconditions: input dictionary must be book_category_dictionary('google_books_dataset.csv') and this file must be saved in the same folder as the google_books_dataset.csv file and T051_P1_load_data.py (case 1 function file).
    >>> get_books_by_rate(book_category_dictionary('google_books_dataset.csv') , 3)   
    There are 8 whose rate is between 3 and 4. This is the list of books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2: Bring Me Back by B A Paris
    Book 3: Mrs. Pollifax Unveiled by Dorothy Gilman
    Book 4: How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 5: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 6: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book 7: The Infinite Game by Simon Sinek
    Book 8: Selling 101: What Every Successful Sales Professional Needs to Know by Zig Ziglar
    8
    >>> get_books_by_rate(book_category_dictionary('google_books_dataset.csv') , 5)
    There are 5 whose rate is between 5 and 6. This is the list of books:
    Book 1: Final Option: 'The best one yet' by Clive Cussler
    Book 2: The Red Signal: An Agatha Christie Short Story by Agatha Christie
    Book 3: Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk by Michael Sincere
    Book 4: Tall Tales and Wee Stories: The Best of Billy Connolly by Billy Connolly
    Book 5: No One Is Too Small to Make a Difference by Greta Thunberg
    5
    >>> get_books_by_rate(book_category_dictionary('google_books_dataset.csv') , 2)
    There are 0 whose rate is between 2 and 3. This is the list of books:
    0
    """
    
        
    if 0 <= rate <= 5:  
        used_books=[]
        counter=1
        for book_list in input_dict.values():
            for book in book_list:      
                if book['rating']!='N/A':
                    if rate <= float(book['rating']) < (rate+1):
                        if (book['title'], book['author']) not in used_books:
                            used_books+=[(book['title'], book['author'])]                    
                
        print('There are', str(len(used_books)), 'whose rate is between', str(rate), 'and', str(rate+1)+'.', 'This is the list of books:')
        for book in used_books:
            print('Book', str(counter)+':', book[0], 'by', book[1])
            counter += 1
    else:
        print('Please enter a rating between 0 and 5.')
    return counter-1


#Function 5 - get_books_by_title (Written by  Leena Ford 101229281)


def get_books_by_title(used_dictionary:dict, title_of_book:str) -> bool:

    """ 
    Returns either True or False based on whether or not a book title is found in the dictionary that we're using to search through (returned from the book_category_dictionary function). Also displays "The book has been found" if it has been found, otherwise displays "The book has NOT been found".
    
    Preconditions: to search through the dictionary returned from the function in case 1, pass 'book_category_dictionary("google_books_dataset.csv")' as the used_dictionary argument. Ensure that the book_category_dictionary python file is in the same folder as your file with the get_books_by_title function. 
    
    
    >>> get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"The Memoirs of Sherlock Holmes")
    The book has been found
    True
    
    >>> get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"The Painted Man (The Demon Cycle. Book 1)")
    The book has been found
    True
    
    >>> get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"the painted man (The Demon Cycle. Book 1)") # title with typo
    The book has NOT been found
    False
    
    >>> get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"Random Book")
    The book has NOT been found
    False
    
    
    """
    
    
    set_of_titles = set()               # Placing all titles in a set to remove duplicates

    for information_list in used_dictionary.values():

        for each_dictionary in information_list:
            titles = each_dictionary.get('title')
           
            if titles not in set_of_titles:
                set_of_titles.add(titles)
    
            
    if title_of_book in set_of_titles:          # Searching in our titles set
        result = True 
        print("The book has been found")
    else:
        result = False
        print("The book has NOT been found")

                    
 
    return result                               # Returns the boolean


#Function 6 - get_books_by_author (Written by Espen Swift 101232582)


def get_books_by_author(input_dict: dict, author_name: str)-> int:
    """
    Returns the number of books written by a specified author, as well as the title and rate of said books below it.
    Preconditions: input dictionary must be book_category_dictionary('google_books_dataset.csv') and this file must be saved in the same folder as the google_books_dataset.csv file and T051_P1_load_data.py (case 1 function file).
    >>> get_books_by_author(book_category_dictionary('google_books_dataset.csv'), 'Barbara Allan')
    The author Barbara Allan has published the following books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery, rate: 3.3
    Book 2: Antiques Con, rate: 4.8
    Book 3: Antiques Chop, rate: 4.5
    Book 4: Antiques Knock-Off, rate: 4.3
    4
    >>> get_books_by_author(book_category_dictionary('google_books_dataset.csv'), 'Brandon Sanderson')
    The author Brandon Sanderson has published the following books:
    Book 1: Edgedancer: From the Stormlight Archive, rate: 4.8
    Book 2: Mistborn Trilogy: The Final Empire. The Well of Ascension. The Hero of Ages, rate: 4.7
    2
    >>> get_books_by_author(book_category_dictionary('google_books_dataset.csv'), 'Espen Swift')
    The author Espen Swift has published the following books:
    0
    """
    
    print("The author", author_name, "has published the following books:")
    used_books=[]
    count=1
    for book_list in input_dict.values():
        for book in book_list:
            if book['title'] not in used_books:
                if book['author'] == author_name:
                    print("Book", str(count)+":", book['title']+",", "rate:", book['rating'])
                    count+=1
                    used_books+=[book['title']]
    return count-1


#Function 7 - get_books_by_publisher (Written by Umayer Joarder 101227396)


def get_books_by_publisher(imprt2: dict, publisher: str) -> int:
    """
     The function returns the amount of books at the end as a string and the names of books along with their
     authors name,published by a certain publisher.
     The function takes in two input parameters imprt2 and publisher. imprt2 is the dictionary
     from the case1 file, we imported the function definition from the case1 file along with the
     dataset file here. Publisher is the publisher of the books which will return the information for.
     
     Preconditions: Make sure the T051_P1_load_data.py file is in the same folder as this file.
     >>>get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"Kensington Publishing Corp.")
     The Publisher Kensington Publishing Corp. has published the following books:
     Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
     Book 2: Antiques Knock-Off by Barbara Allan
     2
     
     >>>get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"Hachette UK")
     The Publisher Hachette UK has published the following books:
     Book 1: Sword of Destiny: Witcher 2: Tales of the Witcher by Andrzej Sapkowski
     Book 2: The Guardians: The explosive new thriller from international bestseller John Grisham by John Grisham
     Book 3: The Name of the Wind: The Kingkiller Chronicle:Book 1 by Patrick Rothfuss
     Book 4: 'Salem's Lot by Stephen King
     Book 5: No Mercy: The brand new novel from the Queen of Crime by Martina Cole
     Book 6: Shantaram by Gregory David Roberts
     Book 7: The Black Box by Michael Connelly
     Book 8: The Tower of the Swallow: Witcher 6 by Andrzej Sapkowski
     Book 9: The Malady and Other Stories: An Andrzej Sapkowski Sampler by Andrzej Sapkowski
     Book 10: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
     Book 11: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
     Book 12: Shantaram by Gregory David Roberts
     Number of books by this publisher:
     12
     
     >>>get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"Tor Books")
     The Publisher Tor Books has published the following books:
     Book 1: Edgedancer: From the Stormlight Archive by Brandon Sanderson
     Book 2: Mistborn Trilogy: The Final Empire. The Well of Ascension. The Hero of Ages by Brandon Sanderson
     Number of books by this publisher:
     2
     
     >>>get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"HarperCollins UK")
     The Publisher HarperCollins UK has published the following books:
     Book 1: The Painted Man (The Demon Cycle. Book 1) by Peter V. Brett
     Book 2: After Anna by Alex Lake
     Book 3: Bring Me Back by B A Paris
     Book 4: The Red Signal: An Agatha Christie Short Story by Agatha Christie
     Book 5: And Then There Were None by Agatha Christie
     Book 6: The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King by J. R. R. Tolkien
     Book 7: A Feast for Crows (A Song of Ice and Fire. Book 4) by George R.R. Martin
     Book 8: A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire) by George R.R. Martin
     Book 9: The Mysterious Affair at Styles by Agatha Christie
     Book 10: Prince of Thorns (The Broken Empire. Book 1) by Mark Lawrence
     Book 11: The Vagrant (The Vagrant Trilogy) by Peter Newman
     Book 12: Predictably Irrational: The Hidden Forces that Shape Our Decisions by Dan Ariely
     Number of books by this publisher:
     12

    
    """
    num3= 0
    publ_lst = []  
    set_pbl = set()
    
    for x4 in imprt2.keys(): 
        for v in range(len(imprt2[x4])):
            if (imprt2[x4][v]["publisher"]) == publisher:
                publ_lst.append(imprt2[x4][v])
    
    for x5 in publ_lst: 
        set_pbl.add(x5["title"])
        
    num3 = len(set_pbl) 

    print("\nThe Publisher", publisher, "has published the following books:")
    
    for x6 in range(len(set_pbl)):
        v2 = x6+1
        print("Book "+str(v2)+": "+str(publ_lst[x6]["title"])+" by "+str(publ_lst[x6]["author"]))
          
    print("Number of books by this publisher:")   
    return num3


#Function 8 - get_all_categories_for_book_title (Written by Leena Ford 101229281) 


def get_all_categories_for_book_title(used_dictionary:dict, title_of_book:str) -> int:
    
    """
    Returns the number of categories associated with the title of the book, found in the used_dictionary (returned from the book_category_dictionary function). Also displays which category that the book title belongs to.
    
    Preconditions: to search through the dictionary returned from the function in case 1, pass 'book_category_dictionary("google_books_dataset.csv")' as the used_dictionary argument. Ensure that the book_category_dictionary is in the same folder as your file with the get_all_categories_for_book_title function. 
    
    >>> get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Tall Tales and Wee Stories: The Best of Billy Connolly")
    The book title " Tall Tales and Wee Stories: The Best of Billy Connolly " belongs to the following categories:
    Category 1 : Humor
    Category 2 : Biography
    2
    
    >>> get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)")
    The book title " Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2) " belongs to the following categories:
    Category 1 : Detective
    Category 2 : Mystery
    Category 3 : Thrillers
    3
    
    >>> get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"riley paige mystery bundle: Once Gone (#1) and Once Taken (#2)")   # Title with typo
    The book title " riley paige mystery bundle: Once Gone (#1) and Once Taken (#2) " belongs to the following categories:
    Sorry, that book does not actually exist in this dictionary
    0
    
    >>> get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Crazy random title")
    The book title " Crazy random title " belongs to the following categories:
    Sorry, that book does not actually exist in this dictionary
    0
    """
    
    category_counter = 0

    print('The book title', '"', title_of_book, '"', 'belongs to the following categories:')
    
    list_of_titles = []
    
    
    for information_list in used_dictionary.values():           # Searching in the values of the dictionary

        for each_dictionary in information_list:
            titles = each_dictionary.get('title')
           
           
            if titles == title_of_book:
                list_of_titles.append(title_of_book)        # organizing the titles in a list 
                category_counter += 1
                print("Category", category_counter,":", each_dictionary.get('category'))
          
                 
    if title_of_book not in list_of_titles:
        print("Sorry, that book does not actually exist in this dictionary")
            
       
    
    return category_counter            # returning the number of categories associated with each book


#The test functions

# Check_equal unit testing function


def check_equal(description: str, outcome, expected) -> bool:
    """
    If the test passes, "PASSED" is displayed. Otherwise, "FAILED" is displayed. 
    
    "description" describes the function call of the function we are testing.
    
    The actual value returned from the function that we're testing is the 'outcome' (actual) 
    and the 'expected' value is what we predict the function should return. 
    
    Preconditions: both the parameters should be the same type. This function should 
    not be used to evaluate whether or not floats/lists of floats/tuples of floats are equal. 
    """
   
    
    outcome_type = type(outcome)
    expected_type = type(expected)
    
    if outcome_type != expected_type:
        
        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        return False
    
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        return False
    
    else:
        print("{0} PASSED".format(description))
        return True
        
    print("------")


#Main script with automated testing

# Test calling

if __name__ == '__main__':
    total_tests = 0
    passed_tests = 0

    passed_tests += check_equal('add_book (where category exists)', add_book(book_category_dictionary('google_books_dataset.csv'), ('My Title', 'Isabella', 'English', 'Fotiainc', 'Fiction', '2.5', '18')), {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Fiction', 'language': 'English'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'category': 'Fiction', 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'category': 'Fiction', 'language': 'English'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'category': 'Fiction', 'language': 'English'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'rating': 4.8, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Fiction', 'language': 'English'}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208, 'category': 'Fiction', 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 1216, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Fiction', 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Fiction', 'language': 'English'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60, 'category': 'Fiction', 'language': 'English'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'rating': 4.3, 'publisher': 'Macmillan', 'pages': 1728, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'category': 'Fiction', 'language': 'English'}, {'title': 'My Title', 'author': 'Isabella', 'language': 'English', 'publisher': 'Fotiainc', 'category': 'Fiction', 'rating': '2.5', 'pages': '18'}], 'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'category': 'Comics', 'language': 'English'}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'pages': 144, 'category': 'Comics', 'language': 'English'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': 128, 'category': 'Comics', 'language': 'English'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': 448, 'category': 'Comics', 'language': 'English'}, {'title': 'The Joker', 'author': 'Brian Azzarello', 'rating': 4.4, 'publisher': 'DC', 'pages': 130, 'category': 'Comics', 'language': 'English'}, {'title': 'Venomized', 'author': 'Cullen Bunn', 'rating': 4.5, 'publisher': 'Marvel Entertainment', 'pages': 136, 'category': 'Comics', 'language': 'English'}], 'Economics': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Economics', 'language': 'English'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Economics', 'language': 'English'}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'pages': 288, 'category': 'Economics', 'language': 'English'}, {'title': 'The Power of Habit: Why We Do What We Do in Life and Business', 'author': 'Charles Duhigg', 'rating': 4.1, 'publisher': 'Random House', 'pages': 416, 'category': 'Economics', 'language': 'English'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Economics', 'language': 'English'}, {'title': 'Getting Things Done: The Art of Stress-Free Productivity', 'author': 'David Allen', 'rating': 4.5, 'publisher': 'Penguin', 'pages': 352, 'category': 'Economics', 'language': 'English'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'pages': 176, 'category': 'Economics', 'language': 'English'}, {'title': 'Rework', 'author': 'Jason Fried', 'rating': 4.1, 'publisher': 'Currency', 'pages': 288, 'category': 'Economics', 'language': 'English'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Economics', 'language': 'English'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'category': 'Economics', 'language': 'English'}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Economics', 'language': 'English'}, {'title': 'Principles: Life and Work', 'author': 'Ray Dalio', 'rating': 4.7, 'publisher': 'Simon and Schuster', 'pages': 592, 'category': 'Economics', 'language': 'English'}, {'title': 'The Magic of Thinking Big', 'author': 'David J. Schwartz', 'rating': 4.6, 'publisher': 'Penguin', 'pages': 256, 'category': 'Economics', 'language': 'English'}, {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'author': 'Steven D. Levitt', 'rating': 3.8, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Economics', 'language': 'English'}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'rating': 5.0, 'publisher': 'Simon and Schuster', 'pages': 224, 'category': 'Economics', 'language': 'English'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304, 'category': 'Economics', 'language': 'English'}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'rating': 4.7, 'publisher': 'Berrett-Koehler Publishers', 'pages': 144, 'category': 'Economics', 'language': 'English'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pages': 14, 'category': 'Economics', 'language': 'English'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Economics', 'language': 'English'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 320, 'category': 'Economics', 'language': 'English'}, {'title': 'Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports', 'author': 'Thomas Ittelson', 'rating': 4.0, 'publisher': 'Red Wheel/Weiser', 'pages': 288, 'category': 'Economics', 'language': 'English'}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'rating': 4.6, 'publisher': 'HarperCollins Leadership', 'pages': 288, 'category': 'Economics', 'language': 'English'}], 'Business': [{'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'category': 'Business', 'language': 'English'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'pages': 176, 'category': 'Business', 'language': 'English'}, {'title': 'Principles: Life and Work', 'author': 'Ray Dalio', 'rating': 4.7, 'publisher': 'Simon and Schuster', 'pages': 592, 'category': 'Business', 'language': 'English'}, {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'rating': 4.5, 'publisher': 'W. W. Norton & Company', 'pages': 256, 'category': 'Business', 'language': 'English'}, {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'rating': 3.8, 'publisher': 'Penguin', 'pages': 272, 'category': 'Business', 'language': 'English'}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'rating': 4.7, 'publisher': 'Berrett-Koehler Publishers', 'pages': 144, 'category': 'Business', 'language': 'English'}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Business', 'language': 'English'}, {'title': 'Selling 101: What Every Successful Sales Professional Needs to Know', 'author': 'Zig Ziglar', 'rating': 3.8, 'publisher': 'HarperCollins Leadership', 'pages': 112, 'category': 'Business', 'language': 'English'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Business', 'language': 'English'}, {'title': 'The Magic of Thinking Big', 'author': 'David J. Schwartz', 'rating': 4.6, 'publisher': 'Penguin', 'pages': 256, 'category': 'Business', 'language': 'English'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304, 'category': 'Business', 'language': 'English'}, {'title': 'Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain', 'author': 'Steven D. Levitt', 'rating': 4.3, 'publisher': 'Harper Collins', 'pages': 304, 'category': 'Business', 'language': 'English'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Business', 'language': 'English'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pages': 14, 'category': 'Business', 'language': 'English'}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'rating': 5.0, 'publisher': 'Simon and Schuster', 'pages': 224, 'category': 'Business', 'language': 'English'}, {'title': 'Rework', 'author': 'Jason Fried', 'rating': 4.1, 'publisher': 'Currency', 'pages': 288, 'category': 'Business', 'language': 'English'}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'rating': 4.6, 'publisher': 'HarperCollins Leadership', 'pages': 288, 'category': 'Business', 'language': 'English'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 320, 'category': 'Business', 'language': 'English'}], 'Detective': [{'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Detective', 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'category': 'Detective', 'language': 'English'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Detective', 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'category': 'Detective', 'language': 'English'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Detective', 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': 'Detective', 'language': 'English'}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208, 'category': 'Detective', 'language': 'English'}, {'title': 'Watching (The Making of Riley Paige Book 1)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'category': 'Detective', 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Detective', 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Detective', 'language': 'English'}, {'title': 'Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Detective', 'language': 'English'}], 'Psychology': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Psychology', 'language': 'English'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304, 'category': 'Psychology', 'language': 'English'}], 'Fantasy': [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'category': 'Fantasy', 'language': 'English'}, {'title': 'Mistborn Trilogy: The Final Empire. The Well of Ascension. The Hero of Ages', 'author': 'Brandon Sanderson', 'rating': 4.7, 'publisher': 'Tor Books', 'pages': 1712, 'category': 'Fantasy', 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fantasy', 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 1216, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fantasy', 'language': 'English'}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fantasy', 'language': 'English'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226, 'category': 'Fantasy', 'language': 'English'}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fantasy', 'language': 'English'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'rating': 4.3, 'publisher': 'Macmillan', 'pages': 1728, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fantasy', 'language': 'English'}], 'Humor': [{'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'category': 'Humor', 'language': 'English'}, {'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'pages': 112, 'category': 'Humor', 'language': 'English'}], 'Crime': [{'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'category': 'Crime', 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Crime', 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'category': 'Crime', 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'category': 'Crime', 'language': 'English'}], 'Thriller': '', 'Mystery': [{'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Mystery', 'language': 'English'}, {'title': 'Watching (The Making of Riley Paige Book 1)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Mystery', 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Mystery', 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Mystery', 'language': 'English'}, {'title': 'Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Mystery', 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'category': 'Mystery', 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'category': 'Mystery', 'language': 'English'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': 'Mystery', 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'category': 'Mystery', 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Mystery', 'language': 'English'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Mystery', 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'category': 'Mystery', 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'category': 'Mystery', 'language': 'English'}], 'Classic': '', 'Adventure': [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Adventure', 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Adventure', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Adventure', 'language': 'English'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'category': 'Adventure', 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'category': 'Adventure', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Adventure', 'language': 'English'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'category': 'Adventure', 'language': 'English'}], 'Superhero': '', 'Biography': [{'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352, 'category': 'Biography', 'language': 'English'}, {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'rating': 5.0, 'publisher': 'Penguin', 'pages': 112, 'category': 'Biography', 'language': 'English'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'category': 'Biography', 'language': 'English'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'rating': 4.6, 'publisher': 'Metropolitan Books', 'pages': 352, 'category': 'Biography', 'language': 'English'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'category': 'Biography', 'language': 'English'}], 'Social Science': [{'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'rating': 4.2, 'publisher': 'Vintage', 'pages': 32, 'category': 'Social Science', 'language': 'English'}, {'title': 'Happy: Why More or Less Everything is Absolutely Fine', 'author': 'Derren Brown', 'rating': 4.0, 'publisher': 'Random House', 'pages': 576, 'category': 'Social Science', 'language': 'English'}, {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'author': 'Steven D. Levitt', 'rating': 3.8, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Social Science', 'language': 'English'}], 'Mythical': '', 'Epic': [{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Epic', 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Epic', 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'category': 'Epic', 'language': 'English'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'category': 'Epic', 'language': 'English'}], 'Horror': [{'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Horror', 'language': 'English'}], 'Traditional': [{'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Traditional', 'language': 'English'}], 'Finance': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Finance', 'language': 'English'}], 'Legal': [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Legal', 'language': 'English'}], 'Management': [{'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Management', 'language': 'English'}], 'Money Management': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Money Management', 'language': 'English'}], 'Information Techonlogy': '', 'Investing': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Investing', 'language': 'English'}], 'Thrillers': [{'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Thrillers', 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Thrillers', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Thrillers', 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': 'Thrillers', 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Thrillers', 'language': 'English'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 416, 'category': 'Thrillers', 'language': 'English'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'category': 'Thrillers', 'language': 'English'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Thrillers', 'language': 'English'}], 'Classics': [{'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Classics', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Classics', 'language': 'English'}], 'Superheroes': [{'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'rating': 4.0, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Superheroes', 'language': 'English'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': 448, 'category': 'Superheroes', 'language': 'English'}, {'title': 'Spider-Verse: Volume 1', 'author': 'Dan Slott', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': 624, 'category': 'Superheroes', 'language': 'English'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'category': 'Superheroes', 'language': 'English'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': 128, 'category': 'Superheroes', 'language': 'English'}], 'Mythical Creatures': [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Mythical Creatures', 'language': 'English'}], 'Information Technology': [{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'category': 'Information Technology', 'language': 'English'}]}
)
    total_tests += 1
    
    passed_tests += check_equal('remove_book (where book exists in dict)', remove_book(book_category_dictionary('google_books_dataset.csv'), "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Fiction'), {'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Fiction', 'language': 'English'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'category': 'Fiction', 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'category': 'Fiction', 'language': 'English'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'category': 'Fiction', 'language': 'English'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'rating': 4.8, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Fiction', 'language': 'English'}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208, 'category': 'Fiction', 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 1216, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Fiction', 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Fiction', 'language': 'English'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60, 'category': 'Fiction', 'language': 'English'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'rating': 4.3, 'publisher': 'Macmillan', 'pages': 1728, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'category': 'Fiction', 'language': 'English'}], 'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'category': 'Comics', 'language': 'English'}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'pages': 144, 'category': 'Comics', 'language': 'English'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': 128, 'category': 'Comics', 'language': 'English'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': 448, 'category': 'Comics', 'language': 'English'}, {'title': 'The Joker', 'author': 'Brian Azzarello', 'rating': 4.4, 'publisher': 'DC', 'pages': 130, 'category': 'Comics', 'language': 'English'}, {'title': 'Venomized', 'author': 'Cullen Bunn', 'rating': 4.5, 'publisher': 'Marvel Entertainment', 'pages': 136, 'category': 'Comics', 'language': 'English'}], 'Economics': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Economics', 'language': 'English'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Economics', 'language': 'English'}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'pages': 288, 'category': 'Economics', 'language': 'English'}, {'title': 'The Power of Habit: Why We Do What We Do in Life and Business', 'author': 'Charles Duhigg', 'rating': 4.1, 'publisher': 'Random House', 'pages': 416, 'category': 'Economics', 'language': 'English'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Economics', 'language': 'English'}, {'title': 'Getting Things Done: The Art of Stress-Free Productivity', 'author': 'David Allen', 'rating': 4.5, 'publisher': 'Penguin', 'pages': 352, 'category': 'Economics', 'language': 'English'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'pages': 176, 'category': 'Economics', 'language': 'English'}, {'title': 'Rework', 'author': 'Jason Fried', 'rating': 4.1, 'publisher': 'Currency', 'pages': 288, 'category': 'Economics', 'language': 'English'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Economics', 'language': 'English'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'category': 'Economics', 'language': 'English'}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Economics', 'language': 'English'}, {'title': 'Principles: Life and Work', 'author': 'Ray Dalio', 'rating': 4.7, 'publisher': 'Simon and Schuster', 'pages': 592, 'category': 'Economics', 'language': 'English'}, {'title': 'The Magic of Thinking Big', 'author': 'David J. Schwartz', 'rating': 4.6, 'publisher': 'Penguin', 'pages': 256, 'category': 'Economics', 'language': 'English'}, {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'author': 'Steven D. Levitt', 'rating': 3.8, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Economics', 'language': 'English'}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'rating': 5.0, 'publisher': 'Simon and Schuster', 'pages': 224, 'category': 'Economics', 'language': 'English'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304, 'category': 'Economics', 'language': 'English'}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'rating': 4.7, 'publisher': 'Berrett-Koehler Publishers', 'pages': 144, 'category': 'Economics', 'language': 'English'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pages': 14, 'category': 'Economics', 'language': 'English'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Economics', 'language': 'English'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 320, 'category': 'Economics', 'language': 'English'}, {'title': 'Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports', 'author': 'Thomas Ittelson', 'rating': 4.0, 'publisher': 'Red Wheel/Weiser', 'pages': 288, 'category': 'Economics', 'language': 'English'}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'rating': 4.6, 'publisher': 'HarperCollins Leadership', 'pages': 288, 'category': 'Economics', 'language': 'English'}], 'Business': [{'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'category': 'Business', 'language': 'English'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'pages': 176, 'category': 'Business', 'language': 'English'}, {'title': 'Principles: Life and Work', 'author': 'Ray Dalio', 'rating': 4.7, 'publisher': 'Simon and Schuster', 'pages': 592, 'category': 'Business', 'language': 'English'}, {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'rating': 4.5, 'publisher': 'W. W. Norton & Company', 'pages': 256, 'category': 'Business', 'language': 'English'}, {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'rating': 3.8, 'publisher': 'Penguin', 'pages': 272, 'category': 'Business', 'language': 'English'}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'rating': 4.7, 'publisher': 'Berrett-Koehler Publishers', 'pages': 144, 'category': 'Business', 'language': 'English'}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Business', 'language': 'English'}, {'title': 'Selling 101: What Every Successful Sales Professional Needs to Know', 'author': 'Zig Ziglar', 'rating': 3.8, 'publisher': 'HarperCollins Leadership', 'pages': 112, 'category': 'Business', 'language': 'English'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Business', 'language': 'English'}, {'title': 'The Magic of Thinking Big', 'author': 'David J. Schwartz', 'rating': 4.6, 'publisher': 'Penguin', 'pages': 256, 'category': 'Business', 'language': 'English'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304, 'category': 'Business', 'language': 'English'}, {'title': 'Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain', 'author': 'Steven D. Levitt', 'rating': 4.3, 'publisher': 'Harper Collins', 'pages': 304, 'category': 'Business', 'language': 'English'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Business', 'language': 'English'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pages': 14, 'category': 'Business', 'language': 'English'}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'rating': 5.0, 'publisher': 'Simon and Schuster', 'pages': 224, 'category': 'Business', 'language': 'English'}, {'title': 'Rework', 'author': 'Jason Fried', 'rating': 4.1, 'publisher': 'Currency', 'pages': 288, 'category': 'Business', 'language': 'English'}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'rating': 4.6, 'publisher': 'HarperCollins Leadership', 'pages': 288, 'category': 'Business', 'language': 'English'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 320, 'category': 'Business', 'language': 'English'}], 'Detective': [{'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Detective', 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'category': 'Detective', 'language': 'English'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Detective', 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'category': 'Detective', 'language': 'English'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Detective', 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': 'Detective', 'language': 'English'}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208, 'category': 'Detective', 'language': 'English'}, {'title': 'Watching (The Making of Riley Paige Book 1)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'category': 'Detective', 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Detective', 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Detective', 'language': 'English'}, {'title': 'Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Detective', 'language': 'English'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Detective', 'language': 'English'}], 'Psychology': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Psychology', 'language': 'English'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304, 'category': 'Psychology', 'language': 'English'}], 'Fantasy': [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'category': 'Fantasy', 'language': 'English'}, {'title': 'Mistborn Trilogy: The Final Empire. The Well of Ascension. The Hero of Ages', 'author': 'Brandon Sanderson', 'rating': 4.7, 'publisher': 'Tor Books', 'pages': 1712, 'category': 'Fantasy', 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fantasy', 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 1216, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fantasy', 'language': 'English'}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fantasy', 'language': 'English'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226, 'category': 'Fantasy', 'language': 'English'}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fantasy', 'language': 'English'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'rating': 4.3, 'publisher': 'Macmillan', 'pages': 1728, 'category': 'Fantasy', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fantasy', 'language': 'English'}], 'Humor': [{'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'category': 'Humor', 'language': 'English'}, {'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'pages': 112, 'category': 'Humor', 'language': 'English'}], 'Crime': [{'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'category': 'Crime', 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Crime', 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'category': 'Crime', 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'category': 'Crime', 'language': 'English'}], 'Thriller': '', 'Mystery': [{'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Mystery', 'language': 'English'}, {'title': 'Watching (The Making of Riley Paige Book 1)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Mystery', 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Mystery', 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Mystery', 'language': 'English'}, {'title': 'Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Mystery', 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'category': 'Mystery', 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'category': 'Mystery', 'language': 'English'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': 'Mystery', 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Mystery', 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'category': 'Mystery', 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Mystery', 'language': 'English'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Mystery', 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'category': 'Mystery', 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'category': 'Mystery', 'language': 'English'}], 'Classic': '', 'Adventure': [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Adventure', 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Adventure', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Adventure', 'language': 'English'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'category': 'Adventure', 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'category': 'Adventure', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Adventure', 'language': 'English'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'category': 'Adventure', 'language': 'English'}], 'Superhero': '', 'Biography': [{'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352, 'category': 'Biography', 'language': 'English'}, {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'rating': 5.0, 'publisher': 'Penguin', 'pages': 112, 'category': 'Biography', 'language': 'English'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'category': 'Biography', 'language': 'English'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'rating': 4.6, 'publisher': 'Metropolitan Books', 'pages': 352, 'category': 'Biography', 'language': 'English'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'category': 'Biography', 'language': 'English'}], 'Social Science': [{'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'rating': 4.2, 'publisher': 'Vintage', 'pages': 32, 'category': 'Social Science', 'language': 'English'}, {'title': 'Happy: Why More or Less Everything is Absolutely Fine', 'author': 'Derren Brown', 'rating': 4.0, 'publisher': 'Random House', 'pages': 576, 'category': 'Social Science', 'language': 'English'}, {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'author': 'Steven D. Levitt', 'rating': 3.8, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Social Science', 'language': 'English'}], 'Mythical': '', 'Epic': [{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Epic', 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Epic', 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'category': 'Epic', 'language': 'English'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'category': 'Epic', 'language': 'English'}], 'Horror': [{'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Horror', 'language': 'English'}], 'Traditional': [{'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Traditional', 'language': 'English'}], 'Finance': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Finance', 'language': 'English'}], 'Legal': [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Legal', 'language': 'English'}], 'Management': [{'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Management', 'language': 'English'}], 'Money Management': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Money Management', 'language': 'English'}], 'Information Techonlogy': '', 'Investing': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Investing', 'language': 'English'}], 'Thrillers': [{'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Thrillers', 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Thrillers', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Thrillers', 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': 'Thrillers', 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'category': 'Thrillers', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Thrillers', 'language': 'English'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 416, 'category': 'Thrillers', 'language': 'English'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'category': 'Thrillers', 'language': 'English'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60, 'category': 'Thrillers', 'language': 'English'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Thrillers', 'language': 'English'}], 'Classics': [{'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Classics', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Classics', 'language': 'English'}], 'Superheroes': [{'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'rating': 4.0, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Superheroes', 'language': 'English'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': 448, 'category': 'Superheroes', 'language': 'English'}, {'title': 'Spider-Verse: Volume 1', 'author': 'Dan Slott', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': 624, 'category': 'Superheroes', 'language': 'English'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'category': 'Superheroes', 'language': 'English'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': 128, 'category': 'Superheroes', 'language': 'English'}], 'Mythical Creatures': [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Mythical Creatures', 'language': 'English'}], 'Information Technology': [{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'category': 'Information Technology', 'language': 'English'}]}
)
    total_tests += 1
   
    passed_tests += check_equal('get_books_by_category', get_books_by_category(book_category_dictionary('google_books_dataset.csv'), "Economics"), 22)
    total_tests += 1
    passed_tests += check_equal('get_books_by_category', get_books_by_category(book_category_dictionary('google_books_dataset.csv'), "Investing"), 1)
    total_tests += 1
    passed_tests += check_equal('get_books_by_category (not real category)', get_books_by_category(book_category_dictionary('google_books_dataset.csv'), "non-real catg"), 0)
    total_tests += 1
    
    passed_tests += check_equal('get_books_by_rate', get_books_by_rate(book_category_dictionary('google_books_dataset.csv') , 3), 8)
    total_tests += 1
    passed_tests += check_equal('get_books_by_rate', get_books_by_rate(book_category_dictionary('google_books_dataset.csv') , 5), 5)
    total_tests += 1
    passed_tests += check_equal('get_books_by_rate (rate out of range)', get_books_by_rate(book_category_dictionary('google_books_dataset.csv') , 0), 0)
  
    total_tests += 1
    passed_tests += check_equal('get_books_by_title', get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"The Memoirs of Sherlock Holmes"), True)
    total_tests += 1
    passed_tests += check_equal('get_books_by_title', get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"The Painted Man (The Demon Cycle. Book 1)"), True)
    total_tests += 1
    passed_tests += check_equal('get_books_by_title (title with typo)', get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"the painted man (The Demon Cycle. Book 1)"), False)
    total_tests += 1
 
    passed_tests += check_equal('get_books_by_author', get_books_by_author(book_category_dictionary('google_books_dataset.csv'), 'Barbara Allan'), 4)
    total_tests += 1
    passed_tests += check_equal('get_books_by_author', get_books_by_author(book_category_dictionary('google_books_dataset.csv'), 'Brandon Sanderson'), 2)
    total_tests += 1
    passed_tests += check_equal('get_books_by_author (author not in dict)', get_books_by_author(book_category_dictionary('google_books_dataset.csv'), 'Espen Swift'), 0)
    total_tests += 1
    
    passed_tests += check_equal('get_books_by_publisher', get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"Kensington Publishing Corp."), 2)
    total_tests += 1
    passed_tests += check_equal('get_books_by_publisher', get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"Hachette UK"), 12)
    total_tests += 1
    passed_tests += check_equal('get_books_by_publisher', get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"HarperCollins UK"), 12)
    total_tests += 1
    
    passed_tests += check_equal('get_all_categories_for_book_title', get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Tall Tales and Wee Stories: The Best of Billy Connolly"), 2)
    total_tests += 1
    passed_tests += check_equal('get_all_categories_for_book_title', get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)"), 3)
    total_tests += 1
    passed_tests += check_equal('get_all_categories_for_book_title (book does not exist)', get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Crazy random title"), 0)
    total_tests += 1    
    
    failed_tests = total_tests - passed_tests
    print("Results")
    print("Total tests done: ", total_tests)
    print("Total tests passed: ", passed_tests)
    print("Total tests failed: ", failed_tests)



