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
from T051_check_equal import check_equal

#The four functions from P3 - Task 1 (and the dictionary_to_list function that arises from refactoring)

def dictionary_to_list(dataset: dict)->list:
 
    """
    Returns a list where all the book data is stored as dictionaries. If a book is 
    repeated more than once, the book is only repeated once and the categories are merged
    into a list.
    
    Preconditions: the argument for the dataset takes in the dictionary from our case 1
    code which follows the format: book_category_dictionary("google_books_dataset.csv").
    Test_one should be imported from the test cases module.
    
    >>> dictionary_to_list(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction', 'Detective', 'Mystery'], 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction', 'Fantasy', 'Thrillers'], 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': ['Fiction', 'Adventure'], 'language': 'English'}...}]
    
    >>> dictionary_to_list(book_category_dictionary("T051_P3_testcase_one.csv"))
    [{'title': 'The book of fantasy', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Fiction', 'Fantasy'], 'language': 'English'}, {'title': 'A funny story', 'author': 'Daniel', 'rating': 4.4, 'publisher': 'Nan inc', 'pages': 25, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Adventures of Jill', 'author': 'Riley K', 'rating': 2.8, 'publisher': 'Hop inc', 'pages': 100...}]

    """
 
 
    master_list=[]
    title_list=[] 
    
    for category in dataset:
        for book in dataset[category]:
            if book['title'] not in title_list:
                book['category'] = [book['category']]
                master_list+=[book]
                title_list+=[book['title']]
            elif book['title'] in title_list:
                master_list[title_list.index(book['title'])]['category'] += [category]    
                
    return master_list

#Constant for the following sort functions:

list_data = dictionary_to_list(book_category_dictionary("google_books_dataset.csv"))

test_one_list = dictionary_to_list(book_category_dictionary("T051_P3_testcase_one.csv"))

test_two_list = dictionary_to_list(book_category_dictionary("T051_P3_testcase_2.csv"))

test_three_list = dictionary_to_list(book_category_dictionary("T051_P3_testcase_3.csv"))

#Function 1 - sort_books_title (written by Leena Ford 101229281)

def sort_books_title(list_data:list) -> list:
    """
    Returns a list where each book data is stored in a dictionary. The book data is stored in a manner where
    the title of each book is ordered alphabetically. All duplicate books have been merged into
    one book title with multiple categories stored in a category list.
    
    Preconditions: place the T051_P1_load_data.py file in the same directory as the file
    containing this function. The argument in the used_dictionary input is: 'book_category_dictionary("google_books_dataset.csv")'.
    
    
    *Note, the apostrophe character in "'Salem's Lot" precedes the letter 'A' in terms of alphabetical order.
    
    >>> sort_books_title(list_data)
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'category': ['Fiction', 'Thrillers'], 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': ['Fiction', 'Fantasy', 'Adventure', 'Epic'], 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A.....}]
    
    >>> sort_books_title(test_one_list)
    [{'title': 'A funny story', 'author': 'Daniel', 'rating': 4.4, 'publisher': 'Nan inc', 'pages': 25, 'category': ['Fiction', 'Sci-fi', 'Detective'], 'language': 'English'}, {'title': 'Crazy adventure', ...}]

    """
                    
    for i in range(len(list_data)):
        for j in range(0,(len(list_data)-i-1)):
            if list_data[j]['title'] > list_data[j+1]['title']:
                list_data[j], list_data[j+1] = list_data[j+1] , list_data[j] 
    
    return list_data  


#Function 2 - sort_books_publisher (written by Umayer Joarder 101227396)

def sort_books_publisher(list_data: list) -> list:
    """
    Preconditions: Place the T051_P3_load_data in the same folder as this file.
    
    Returns a list where the books are sorted alphabetically by the publisher, and in a dictionary.
     >>> sort_books_publisher(list_data) 
     [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': ['Economics', 'Business'], 'language': 'English'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': ['Economics', 'Management'], 'language': 'English'}...}]
     
     >>> sort_books_publisher(test_one_list)
    [{'title': "Jill's Adventures", 'author': 'Riley', 'rating': 2.8, 'publisher': 'Hop inc', 'pages': 100, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Trying to succeed', 'author': 'Riley', 'rating': 2.8, 'publisher': 'Hop inc', 'pages': 100, 'category': ['Fantasy'], 'language': 'English'}, {'title': 'The book of fantasy', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc'...}]

    """
   
    list_len = len(list_data)
    for i in range(list_len):
        for j in range(list_len - i - 1):
            if list_data[j]['publisher'] > list_data[j+1]['publisher']: 
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
            if list_data[j]['publisher'] == list_data[j+1]['publisher']: 
                if list_data[j]['title'] > list_data[j+1]['title']:
                    list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
    return  list_data

#Function 3 - sort_books_author (written by Espen Swift 101232582)

def sort_books_author(list_data: list)->list:
    """
    Returns a list of all books contained within the dataset sorted by authors in alphabetical order. If an author has written multiple books then their books will be listed by title in aphabetical order.
    Preconditions: input dataset must be: book_category_dictionary("google_books_dataset.csv"), and the T051_P1_load_data.py file must be contained within the same folder as this file for succesful imports
    
    >>> sort_books_author(list_data)
    [{'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'pages': 112, 'category': ['Humor'], 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': ['Fiction', 'Detective', 'Mystery', 'Thrillers'], 'language': 'English'}, ... , {'title': 'Selling 101: What Every Successful Sales Professional Needs to Know', 'author': 'Zig Ziglar', 'rating': 3.8, 'publisher': 'HarperCollins Leadership', 'pages': 112, 'category': ['Business'], 'language': 'English'}]
    
    >>> sort_books_author(test_one_list)
    [{'title': 'Trying', 'author': 'Alisha', 'rating': 1.9, 'publisher': 'Yes in', 'pages': 112, 'category': ['Detective'], 'language': 'English'}, {'title': 'Murdoch', 'author': 'Cynthia', 'rating': 8.0, 'publisher': 'Talent inc', 'pages': 82, 'category': ['Detective'], 'language': 'English'}, {'title': 'A funny story', 'author': 'Daniel', 'rating': 4.4, 'publisher': 'Nan inc', 'pages': 25, 'category': ['Fiction', 'Sci-fi', 'Detective'], 'language': 'English'}, {'title': 'Here home', 'author': 'Girl', 'rating': 1.4, 'publisher': 'Tool inc', 'pages': 80, 'category': ['Sci-fi'], 'language': 'English'}, {'title': 'Fofa world', 'author': 'Jaden'...}]
    """
    
    for i in range(len(list_data)):
        for j in range(0, len(list_data)-i-1):
            if list_data[j]['author'] > list_data[j+1]['author']:
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
            elif list_data[j]['author'] == list_data[j+1]['author']:
                if list_data[j]['title'] > list_data[j+1]['title']:
                    list_data[j], list_data[j+1]= list_data[j+1], list_data[j]

    return list_data


#Function 4 sort_books_ascending_rate (written by Isabella Fotia 101228368) 

def sort_books_ascending_rate(list_data: list)->list:
    """
    Returns a list where the book data is stored in a dictionary. In the list, the books are stored by rate in ascending order. If two (or more) books have the
    same rate, then the books are stored based on book title in alphabetical order.
    
     Preconditions: input dataset must be: book_category_dictionary("google_books_dataset.csv"), and the T051_P1_load_data.py file must be contained within the same folder as this file.
    
    >>> sort_books_ascending_rate(list_data)
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': ['Economics', 'Business'], 'language': 'English'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'category': ['Economics', 'Management'], 'language': 'English'}...}]
    
    >>> sort_books_ascending_rate(test_one_list)
    [{'title': 'The book of fantasy', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Fiction', 'Fantasy', 'Sci-fi', 'Detective'], 'language': 'English'}, {'title': 'Here home', 'author': 'Girl', 'rating': 1.4, 'publisher': 'Tool inc', 'pages': 80, 'category': ['Sci-fi'], 'language': 'English'}, {'title': 'Trying', 'author': 'Alisha', 'rating': 1.9, 'publisher': 'Yes in', 'pages': 112, 'category': ['Detective'], 'language': 'English'}, {'title': 'Fofa world', 'author': 'Jaden', 'rating': 2.2, 'publisher': 'Yes inc', 'pages': 350, 'category': ['Fantasy'], 'language': 'English'}, {'title': "Jill's Adventures", 'author': 'Riley', 'rating': 2.8, 'publisher': 'Hop inc', 'pages': 100, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Trying to succeed', 'author': 'Riley', 'rating': 2.8, 'publisher': 'Hop inc', 'pages': 100, 'category': ['Fantasy'], 'language': 'English'}, {'title': 'Detective show', 'author': 'Zola', 'rating': 3.9, 'publisher': 'Weird inc', 'pages': 200, 'category': ['Detective'], 'language': 'English'}, {'title': 'Mystery inc', 'author': 'Tammy', 'rating': 4.0...}]

    """
    
    
    for i in range(len(list_data)):
        for j in range(0, len(list_data)-i-1):
            if (list_data[j]['rating'] =='N/A') and (list_data[j+1]['rating']=='N/A'):
                if list_data[j]['title'] > list_data[j+1]['title']:
                    list_data[j], list_data[j+1]= list_data[j+1], list_data[j]                               
            elif list_data[j]['rating']=='N/A' and list_data[j+1]['rating']!='N/A':
                None
            elif list_data[j]['rating']!='N/A' and list_data[j+1]['rating']=='N/A':
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
            elif list_data[j]['rating']=='N/A' and list_data[j+1]['rating']=='N/A':
                None
            elif list_data[j]['rating'] > list_data[j+1]['rating']:
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]


        
    return list_data

  
#Main script with automated testing


if __name__ == '__main__':
    total_tests = 0
    passed_tests = 0
   
    passed_tests += check_equal('Testing sort_books_title with test case 1', sort_books_title(test_one_list), [{'title': 'A funny story', 'author': 'Daniel', 'rating': 4.4, 'publisher': 'Nan inc', 'pages': 25, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Adventures of Jill', 'author': 'Riley K', 'rating': 2.8, 'publisher': 'Hop inc', 'pages': 100, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Crazy Adventure', 'author': 'Tom', 'rating': 4.5, 'publisher': 'Tiger inc', 'pages': 40, 'category': ['Fantasy'], 'language': 'English'}, {'title': 'Detective Book', 'author': 'Zayna', 'rating': 3.9, 'publisher': 'Weird inc', 'pages': 200, 'category': ['Detective'], 'language': 'English'}, {'title': 'Imaginary World', 'author': 'Jaden', 'rating': 2.2, 'publisher': 'Yesterday inc', 'pages': 350, 'category': ['Fantasy'], 'language': 'English'}, {'title': 'Mystery Town', 'author': 'Cynthia', 'rating': 3.1, 'publisher': 'Talent inc', 'pages': 82, 'category': ['Detective'], 'language': 'English'}, {'title': 'Scooby Doo', 'author': 'Tammy', 'rating': 4.1, 'publisher': 'Nan inc', 'pages': 26, 'category': ['Detective'], 'language': 'English'}, {'title': 'Successful Book', 'author': 'Jaden', 'rating': 3.9, 'publisher': 'Tool inc', 'pages': 210, 'category': ['Fiction'], 'language': 'English'}, {'title': 'The book of fantasy', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Fiction', 'Fantasy'], 'language': 'English'}, {'title': 'Trying something new', 'author': 'Alisha', 'rating': 1.9, 'publisher': 'Yesterday inc', 'pages': 112, 'category': ['Detective'], 'language': 'English'}])
    
    total_tests += 1
    
    passed_tests += check_equal('Testing sort_books_title with test case 2', sort_books_title(test_two_list), [{'title': 'A Thrillers book', 'author': 'Marrel Bee', 'rating': 'N/A', 'publisher': 'Publisher corporation', 'pages': 210, 'category': ['Thrillers'], 'language': 'English'}, {'title': 'A humor Story', 'author': 'Corey', 'rating': 4.4, 'publisher': 'Books stories inc', 'pages': 25, 'category': ['Humor'], 'language': 'English'}, {'title': 'Carrie and her adventure', 'author': 'John Doe', 'rating': 4.6, 'publisher': 'Unknown inc', 'pages': 250, 'category': ['Comics'], 'language': 'English'}, {'title': 'Frozen', 'author': 'Nick S', 'rating': 2.8, 'publisher': 'Ice inc', 'pages': 100, 'category': ['Comics', 'Thrillers'], 'language': 'English'}, {'title': 'Harry Potter new book', 'author': 'Cynthia', 'rating': 2.1, 'publisher': 'Talent inc', 'pages': 81, 'category': ['Humor', 'Mystery'], 'language': 'English'}, {'title': 'Mystery group', 'author': 'Marrel Bee', 'rating': 4.6, 'publisher': 'No one inc', 'pages': 26, 'category': ['Mystery'], 'language': 'English'}, {'title': 'Over the water', 'author': 'Marrel Bee', 'rating': 'N/A', 'publisher': 'Publisher corporation', 'pages': 210, 'category': ['Humor'], 'language': 'English'}, {'title': 'The book of death', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Mystery'], 'language': 'English'}, {'title': 'The duck in the pond', 'author': 'Duckee M', 'rating': 4.6, 'publisher': 'Duck inc', 'pages': 225, 'category': ['Comics', 'Thrillers'], 'language': 'English'}])
    
    total_tests += 1
    
    passed_tests += check_equal('Testing sort_books_title with test case 3', sort_books_title(test_three_list), [{'title': 'Adventures of Tom and Jerry', 'author': 'Disney Author', 'rating': 3.2, 'publisher': 'Disney', 'pages': 203, 'category': ['Adventure', 'Superheroes'], 'language': 'English'}, {'title': 'Bank dollars', 'author': 'Bank Joe', 'rating': 1.3, 'publisher': 'Paper inc', 'pages': 26, 'category': ['Economics'], 'language': 'English'}, {'title': 'Batman van', 'author': 'Marvel Man', 'rating': 2.3, 'publisher': 'Bat inc', 'pages': 10, 'category': ['Adventure', 'Superheroes'], 'language': 'English'}, {'title': 'Gerry Biography', 'author': 'Corey', 'rating': 1.3, 'publisher': 'Books stories inc', 'pages': 25, 'category': ['Biography'], 'language': 'English'}, {'title': 'Green Lantern', 'author': 'Marvel Man', 'rating': 4.9, 'publisher': 'Movie book inc', 'pages': 12, 'category': ['Superheroes'], 'language': 'English'}, {'title': 'Money is green', 'author': 'Bill Gates', 'rating': 2.5, 'publisher': 'Disney', 'pages': 26, 'category': ['Economics'], 'language': 'English'}, {'title': 'Monkey on the vine', 'author': 'Curious George', 'rating': 1.3, 'publisher': 'Nickelodeon', 'pages': 212, 'category': ['Adventure'], 'language': 'English'}, {'title': 'Value of money', 'author': 'Adam May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Economics', 'Adventure'], 'language': 'English'}, {'title': 'Waves in Oceans', 'author': 'Water person', 'rating': 4.9, 'publisher': 'Books stories inc', 'pages': 300, 'category': ['Economics', 'Economics', 'Adventure'], 'language': 'English'}])
    
    total_tests += 1
    
    passed_tests += check_equal('Testing sort_books_publisher with test case 1', sort_books_publisher(test_one_list), [{'title': 'Adventures of Jill', 'author': 'Riley K', 'rating': 2.8, 'publisher': 'Hop inc', 'pages': 100, 'category': ['Fiction'], 'language': 'English'}, {'title': 'The book of fantasy', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Fiction', 'Fantasy'], 'language': 'English'}, {'title': 'A funny story', 'author': 'Daniel', 'rating': 4.4, 'publisher': 'Nan inc', 'pages': 25, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Scooby Doo', 'author': 'Tammy', 'rating': 4.1, 'publisher': 'Nan inc', 'pages': 26, 'category': ['Detective'], 'language': 'English'}, {'title': 'Mystery Town', 'author': 'Cynthia', 'rating': 3.1, 'publisher': 'Talent inc', 'pages': 82, 'category': ['Detective'], 'language': 'English'}, {'title': 'Crazy Adventure', 'author': 'Tom', 'rating': 4.5, 'publisher': 'Tiger inc', 'pages': 40, 'category': ['Fantasy'], 'language': 'English'}, {'title': 'Successful Book', 'author': 'Jaden', 'rating': 3.9, 'publisher': 'Tool inc', 'pages': 210, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Detective Book', 'author': 'Zayna', 'rating': 3.9, 'publisher': 'Weird inc', 'pages': 200, 'category': ['Detective'], 'language': 'English'}, {'title': 'Imaginary World', 'author': 'Jaden', 'rating': 2.2, 'publisher': 'Yesterday inc', 'pages': 350, 'category': ['Fantasy'], 'language': 'English'}, {'title': 'Trying something new', 'author': 'Alisha', 'rating': 1.9, 'publisher': 'Yesterday inc', 'pages': 112, 'category': ['Detective'], 'language': 'English'}]
)
    
    total_tests += 1
    
    passed_tests += check_equal('Testing sort_books_publisher with test case 2', sort_books_publisher(test_two_list), [{'title': 'A humor Story', 'author': 'Corey', 'rating': 4.4, 'publisher': 'Books stories inc', 'pages': 25, 'category': ['Humor'], 'language': 'English'}, {'title': 'The duck in the pond', 'author': 'Duckee M', 'rating': 4.6, 'publisher': 'Duck inc', 'pages': 225, 'category': ['Comics', 'Thrillers'], 'language': 'English'}, {'title': 'Frozen', 'author': 'Nick S', 'rating': 2.8, 'publisher': 'Ice inc', 'pages': 100, 'category': ['Comics', 'Thrillers'], 'language': 'English'}, {'title': 'The book of death', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Mystery'], 'language': 'English'}, {'title': 'Mystery group', 'author': 'Marrel Bee', 'rating': 4.6, 'publisher': 'No one inc', 'pages': 26, 'category': ['Mystery'], 'language': 'English'}, {'title': 'A Thrillers book', 'author': 'Marrel Bee', 'rating': 'N/A', 'publisher': 'Publisher corporation', 'pages': 210, 'category': ['Thrillers'], 'language': 'English'}, {'title': 'Over the water', 'author': 'Marrel Bee', 'rating': 'N/A', 'publisher': 'Publisher corporation', 'pages': 210, 'category': ['Humor'], 'language': 'English'}, {'title': 'Harry Potter new book', 'author': 'Cynthia', 'rating': 2.1, 'publisher': 'Talent inc', 'pages': 81, 'category': ['Humor', 'Mystery'], 'language': 'English'}, {'title': 'Carrie and her adventure', 'author': 'John Doe', 'rating': 4.6, 'publisher': 'Unknown inc', 'pages': 250, 'category': ['Comics'], 'language': 'English'}])
    
    total_tests += 1
    
    passed_tests += check_equal('Testing sort_books_publisher with test case 3', sort_books_publisher(test_three_list), [{'title': 'Batman van', 'author': 'Marvel Man', 'rating': 2.3, 'publisher': 'Bat inc', 'pages': 10, 'category': ['Adventure', 'Superheroes'], 'language': 'English'}, {'title': 'Gerry Biography', 'author': 'Corey', 'rating': 1.3, 'publisher': 'Books stories inc', 'pages': 25, 'category': ['Biography'], 'language': 'English'}, {'title': 'Waves in Oceans', 'author': 'Water person', 'rating': 4.9, 'publisher': 'Books stories inc', 'pages': 300, 'category': ['Economics', 'Economics', 'Adventure'], 'language': 'English'}, {'title': 'Adventures of Tom and Jerry', 'author': 'Disney Author', 'rating': 3.2, 'publisher': 'Disney', 'pages': 203, 'category': ['Adventure', 'Superheroes'], 'language': 'English'}, {'title': 'Money is green', 'author': 'Bill Gates', 'rating': 2.5, 'publisher': 'Disney', 'pages': 26, 'category': ['Economics'], 'language': 'English'}, {'title': 'Green Lantern', 'author': 'Marvel Man', 'rating': 4.9, 'publisher': 'Movie book inc', 'pages': 12, 'category': ['Superheroes'], 'language': 'English'}, {'title': 'Value of money', 'author': 'Adam May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Economics', 'Adventure'], 'language': 'English'}, {'title': 'Monkey on the vine', 'author': 'Curious George', 'rating': 1.3, 'publisher': 'Nickelodeon', 'pages': 212, 'category': ['Adventure'], 'language': 'English'}, {'title': 'Bank dollars', 'author': 'Bank Joe', 'rating': 1.3, 'publisher': 'Paper inc', 'pages': 26, 'category': ['Economics'], 'language': 'English'}])
    
    total_tests += 1
    
    passed_tests += check_equal('Testing sort_books_author with test case 1', sort_books_author(test_one_list), [{'title': 'Trying something new', 'author': 'Alisha', 'rating': 1.9, 'publisher': 'Yesterday inc', 'pages': 112, 'category': ['Detective'], 'language': 'English'}, {'title': 'Mystery Town', 'author': 'Cynthia', 'rating': 3.1, 'publisher': 'Talent inc', 'pages': 82, 'category': ['Detective'], 'language': 'English'}, {'title': 'A funny story', 'author': 'Daniel', 'rating': 4.4, 'publisher': 'Nan inc', 'pages': 25, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Imaginary World', 'author': 'Jaden', 'rating': 2.2, 'publisher': 'Yesterday inc', 'pages': 350, 'category': ['Fantasy'], 'language': 'English'}, {'title': 'Successful Book', 'author': 'Jaden', 'rating': 3.9, 'publisher': 'Tool inc', 'pages': 210, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Adventures of Jill', 'author': 'Riley K', 'rating': 2.8, 'publisher': 'Hop inc', 'pages': 100, 'category': ['Fiction'], 'language': 'English'}, {'title': 'The book of fantasy', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Fiction', 'Fantasy'], 'language': 'English'}, {'title': 'Scooby Doo', 'author': 'Tammy', 'rating': 4.1, 'publisher': 'Nan inc', 'pages': 26, 'category': ['Detective'], 'language': 'English'}, {'title': 'Crazy Adventure', 'author': 'Tom', 'rating': 4.5, 'publisher': 'Tiger inc', 'pages': 40, 'category': ['Fantasy'], 'language': 'English'}, {'title': 'Detective Book', 'author': 'Zayna', 'rating': 3.9, 'publisher': 'Weird inc', 'pages': 200, 'category': ['Detective'], 'language': 'English'}])
    
    total_tests += 1
    
    passed_tests += check_equal('Testing sort_books_author with test case 2', sort_books_author(test_two_list), [{'title': 'A humor Story', 'author': 'Corey', 'rating': 4.4, 'publisher': 'Books stories inc', 'pages': 25, 'category': ['Humor'], 'language': 'English'}, {'title': 'Harry Potter new book', 'author': 'Cynthia', 'rating': 2.1, 'publisher': 'Talent inc', 'pages': 81, 'category': ['Humor', 'Mystery'], 'language': 'English'}, {'title': 'The duck in the pond', 'author': 'Duckee M', 'rating': 4.6, 'publisher': 'Duck inc', 'pages': 225, 'category': ['Comics', 'Thrillers'], 'language': 'English'}, {'title': 'Carrie and her adventure', 'author': 'John Doe', 'rating': 4.6, 'publisher': 'Unknown inc', 'pages': 250, 'category': ['Comics'], 'language': 'English'}, {'title': 'A Thrillers book', 'author': 'Marrel Bee', 'rating': 'N/A', 'publisher': 'Publisher corporation', 'pages': 210, 'category': ['Thrillers'], 'language': 'English'}, {'title': 'Mystery group', 'author': 'Marrel Bee', 'rating': 4.6, 'publisher': 'No one inc', 'pages': 26, 'category': ['Mystery'], 'language': 'English'}, {'title': 'Over the water', 'author': 'Marrel Bee', 'rating': 'N/A', 'publisher': 'Publisher corporation', 'pages': 210, 'category': ['Humor'], 'language': 'English'}, {'title': 'Frozen', 'author': 'Nick S', 'rating': 2.8, 'publisher': 'Ice inc', 'pages': 100, 'category': ['Comics', 'Thrillers'], 'language': 'English'}, {'title': 'The book of death', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Mystery'], 'language': 'English'}])
    
    total_tests += 1
    
    passed_tests += check_equal('Testing sort_books_author with test case 3', sort_books_author(test_three_list), [{'title': 'Value of money', 'author': 'Adam May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Economics', 'Adventure'], 'language': 'English'}, {'title': 'Bank dollars', 'author': 'Bank Joe', 'rating': 1.3, 'publisher': 'Paper inc', 'pages': 26, 'category': ['Economics'], 'language': 'English'}, {'title': 'Money is green', 'author': 'Bill Gates', 'rating': 2.5, 'publisher': 'Disney', 'pages': 26, 'category': ['Economics'], 'language': 'English'}, {'title': 'Gerry Biography', 'author': 'Corey', 'rating': 1.3, 'publisher': 'Books stories inc', 'pages': 25, 'category': ['Biography'], 'language': 'English'}, {'title': 'Monkey on the vine', 'author': 'Curious George', 'rating': 1.3, 'publisher': 'Nickelodeon', 'pages': 212, 'category': ['Adventure'], 'language': 'English'}, {'title': 'Adventures of Tom and Jerry', 'author': 'Disney Author', 'rating': 3.2, 'publisher': 'Disney', 'pages': 203, 'category': ['Adventure', 'Superheroes'], 'language': 'English'}, {'title': 'Batman van', 'author': 'Marvel Man', 'rating': 2.3, 'publisher': 'Bat inc', 'pages': 10, 'category': ['Adventure', 'Superheroes'], 'language': 'English'}, {'title': 'Green Lantern', 'author': 'Marvel Man', 'rating': 4.9, 'publisher': 'Movie book inc', 'pages': 12, 'category': ['Superheroes'], 'language': 'English'}, {'title': 'Waves in Oceans', 'author': 'Water person', 'rating': 4.9, 'publisher': 'Books stories inc', 'pages': 300, 'category': ['Economics', 'Economics', 'Adventure'], 'language': 'English'}])
    
    total_tests += 1
    
    passed_tests += check_equal('Testing sort_books_ascending_rate with test case 1', sort_books_ascending_rate(test_one_list), [{'title': 'The book of fantasy', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Fiction', 'Fantasy'], 'language': 'English'}, {'title': 'Trying something new', 'author': 'Alisha', 'rating': 1.9, 'publisher': 'Yesterday inc', 'pages': 112, 'category': ['Detective'], 'language': 'English'}, {'title': 'Imaginary World', 'author': 'Jaden', 'rating': 2.2, 'publisher': 'Yesterday inc', 'pages': 350, 'category': ['Fantasy'], 'language': 'English'}, {'title': 'Adventures of Jill', 'author': 'Riley K', 'rating': 2.8, 'publisher': 'Hop inc', 'pages': 100, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Mystery Town', 'author': 'Cynthia', 'rating': 3.1, 'publisher': 'Talent inc', 'pages': 82, 'category': ['Detective'], 'language': 'English'}, {'title': 'Successful Book', 'author': 'Jaden', 'rating': 3.9, 'publisher': 'Tool inc', 'pages': 210, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Detective Book', 'author': 'Zayna', 'rating': 3.9, 'publisher': 'Weird inc', 'pages': 200, 'category': ['Detective'], 'language': 'English'}, {'title': 'Scooby Doo', 'author': 'Tammy', 'rating': 4.1, 'publisher': 'Nan inc', 'pages': 26, 'category': ['Detective'], 'language': 'English'}, {'title': 'A funny story', 'author': 'Daniel', 'rating': 4.4, 'publisher': 'Nan inc', 'pages': 25, 'category': ['Fiction'], 'language': 'English'}, {'title': 'Crazy Adventure', 'author': 'Tom', 'rating': 4.5, 'publisher': 'Tiger inc', 'pages': 40, 'category': ['Fantasy'], 'language': 'English'}])
    
    total_tests += 1
     
    passed_tests += check_equal('Testing sort_books_ascending_rate with test case 2', sort_books_ascending_rate(test_two_list), [{'title': 'A Thrillers book', 'author': 'Marrel Bee', 'rating': 'N/A', 'publisher': 'Publisher corporation', 'pages': 210, 'category': ['Thrillers'], 'language': 'English'}, {'title': 'Over the water', 'author': 'Marrel Bee', 'rating': 'N/A', 'publisher': 'Publisher corporation', 'pages': 210, 'category': ['Humor'], 'language': 'English'}, {'title': 'The book of death', 'author': 'Sarah May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Mystery'], 'language': 'English'}, {'title': 'Harry Potter new book', 'author': 'Cynthia', 'rating': 2.1, 'publisher': 'Talent inc', 'pages': 81, 'category': ['Humor', 'Mystery'], 'language': 'English'}, {'title': 'Frozen', 'author': 'Nick S', 'rating': 2.8, 'publisher': 'Ice inc', 'pages': 100, 'category': ['Comics', 'Thrillers'], 'language': 'English'}, {'title': 'A humor Story', 'author': 'Corey', 'rating': 4.4, 'publisher': 'Books stories inc', 'pages': 25, 'category': ['Humor'], 'language': 'English'}, {'title': 'The duck in the pond', 'author': 'Duckee M', 'rating': 4.6, 'publisher': 'Duck inc', 'pages': 225, 'category': ['Comics', 'Thrillers'], 'language': 'English'}, {'title': 'Carrie and her adventure', 'author': 'John Doe', 'rating': 4.6, 'publisher': 'Unknown inc', 'pages': 250, 'category': ['Comics'], 'language': 'English'}, {'title': 'Mystery group', 'author': 'Marrel Bee', 'rating': 4.6, 'publisher': 'No one inc', 'pages': 26, 'category': ['Mystery'], 'language': 'English'}])
    
    total_tests += 1
     
    passed_tests += check_equal('Testing sort_books_ascending_rate with test case 3', sort_books_ascending_rate(test_three_list), [{'title': 'Value of money', 'author': 'Adam May', 'rating': 'N/A', 'publisher': 'Mystery inc', 'pages': 20, 'category': ['Economics', 'Adventure'], 'language': 'English'}, {'title': 'Bank dollars', 'author': 'Bank Joe', 'rating': 1.3, 'publisher': 'Paper inc', 'pages': 26, 'category': ['Economics'], 'language': 'English'}, {'title': 'Gerry Biography', 'author': 'Corey', 'rating': 1.3, 'publisher': 'Books stories inc', 'pages': 25, 'category': ['Biography'], 'language': 'English'}, {'title': 'Monkey on the vine', 'author': 'Curious George', 'rating': 1.3, 'publisher': 'Nickelodeon', 'pages': 212, 'category': ['Adventure'], 'language': 'English'}, {'title': 'Batman van', 'author': 'Marvel Man', 'rating': 2.3, 'publisher': 'Bat inc', 'pages': 10, 'category': ['Adventure', 'Superheroes'], 'language': 'English'}, {'title': 'Money is green', 'author': 'Bill Gates', 'rating': 2.5, 'publisher': 'Disney', 'pages': 26, 'category': ['Economics'], 'language': 'English'}, {'title': 'Adventures of Tom and Jerry', 'author': 'Disney Author', 'rating': 3.2, 'publisher': 'Disney', 'pages': 203, 'category': ['Adventure', 'Superheroes'], 'language': 'English'}, {'title': 'Green Lantern', 'author': 'Marvel Man', 'rating': 4.9, 'publisher': 'Movie book inc', 'pages': 12, 'category': ['Superheroes'], 'language': 'English'}, {'title': 'Waves in Oceans', 'author': 'Water person', 'rating': 4.9, 'publisher': 'Books stories inc', 'pages': 300, 'category': ['Economics', 'Economics', 'Adventure'], 'language': 'English'}])
    
    total_tests += 1
    
    tests_failed = total_tests - passed_tests
    
    print('Results of tests')
    print('Total tests completed:', total_tests)
    print('Total tests passed:', passed_tests)
    print('Total tests failed:', tests_failed)
    
    
    



