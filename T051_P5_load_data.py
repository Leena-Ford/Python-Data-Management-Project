# T051
# Date: 12/04/2022
# Version: 2.0
# Active Members:
# Umayer Joarder 101227396 (Wrote the code initially)
# Leena Ford 101229281 (reviewed the code) 
# Isabella Fotia 101228368 (reviewed the code)
# Espen Swift 101232582 (modified to compensate duplicate books)  

# Function Definition for Case 1  

def book_category_dictionary(filename:str) -> dict: 
    
    
    """ 
    Reads an excel spreadsheet of books and returns a dictionary where each key corresponds to a different book category and each value associated with that category key, consists of a list of books classified in said category.
    
    Preconditions: Must spell the filename correctly. The file should be in the same directory as the python file.
    
    >>> book_category_dictionary("google_books_dataset.csv")
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}...
    
    """    
    
    
    opening = open(filename, "r") # opening the file
      
    
    # List with all the categories
    fiction_list = []
    comics_list = []
    economics_list = []
    business_list = []
    detective_list = []
    psychology_list = []
    fantasy_list = []
    humor_list = []
    crime_list = []
    thriller_list = []
    mystery_list = []
    classic_list = []
    adventure_list = []
    superhero_list = []
    biography_list = []
    social_science_list = []
    mythical_creatures_list = []
    epic_list = []
    horror_list = []
    traditional_list = []
    finance_list = []
    legal_list = []
    management_list = []
    money_management_list = []
    information_technology_list = []
    investing_list = []    
    
    
    book_dictionary = {"Fiction": "", "Comics": "", "Economics": "", "Business": "", "Detective": "", "Psychology": "", "Fantasy": "", "Humor": "", "Crime": "", "Thriller": "", "Mystery": "", "Classic": "", "Adventure": "", "Superhero": "", "Biography": "", "Social Science": "", "Mythical": "", "Epic": "", "Horror": "", "Traditional": "", "Finance": "", "Legal": "", "Management": "", "Money Management": "", "Information Techonlogy": "", "Investing": ""}
      
    used_list=[]
    
    for row in opening: 
        row_box = row.split(',')
             
        
        # Changing the ratings into floats and the pages into integers 
        if (row_box[4] != 'pages'):
            row_box[4] = int(row_box[4])           
        
        if (row_box[2] != 'N/A') and (row_box[2] != 'rating'):
            row_box[2] = float(row_box[2])
        
        # Stripping the '\n'
        row_box[6] = row_box[6].strip('\n')
        
        # Dealing with duplicates
        if row_box not in used_list:
            used_list+=[row_box]
        
            # Adding to our book dictionary  
            if row_box[5] == "Fiction":
                fiction_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Fiction" : fiction_list})
            
            if row_box[5] == 'Comics':
                comics_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Comics" : comics_list})
                
            if row_box[5] == 'Economics':
                economics_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Economics" : economics_list})
                
            if row_box[5] == 'Business':
                business_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Business" : business_list})
                
            if row_box[5] == 'Detective':
                detective_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Detective" : detective_list})
                
            if row_box[5] == 'Psychology':
                psychology_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Psychology" : psychology_list})
                
            if row_box[5] == 'Fantasy':
                fantasy_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Fantasy" : fantasy_list})
                
            if row_box[5] == 'Humor':
                humor_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Humor" : humor_list})
                
            if row_box[5] == 'Crime':
                crime_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Crime" : crime_list})
                
            if row_box[5] == 'Thrillers':
                thriller_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Thrillers" : thriller_list})
                
            if row_box[5] == 'Mystery':
                mystery_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Mystery" : mystery_list})
                
            if row_box[5] == 'Classics':
                classic_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Classics" : classic_list})
                
            if row_box[5] == 'Adventure':
                adventure_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Adventure" : adventure_list})
                
            if row_box[5] == 'Superheroes':
                superhero_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Superheroes" : superhero_list})
                
            if row_box[5] == 'Biography':
                biography_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Biography" : biography_list})
                
            if row_box[5] == 'Social Science':
                social_science_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Social Science" : social_science_list})
                
            if row_box[5] == 'Mythical Creatures':
                mythical_creatures_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Mythical Creatures" : mythical_creatures_list})
                
            if row_box[5] == 'Epic':
                epic_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Epic" : epic_list})
                
            if row_box[5] == 'Horror':
                horror_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Horror" : horror_list})
            
            if row_box[5] == 'Traditional':
                traditional_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Traditional" : traditional_list})
                
            if row_box[5] == 'Finance':
                finance_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Finance" : finance_list})
                
            if row_box[5] == 'Legal':
                legal_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Legal" : legal_list})
                
            if row_box[5] == 'Management':
                management_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Management" : management_list}) 
                
            if row_box[5] == 'Money Management': 
                money_management_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Money Management" : money_management_list})
                
            if row_box[5] == 'Information Technology':
                information_technology_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Information Technology" : information_technology_list})
                
            if row_box[5] == 'Investing':
                investing_list += [{"title": row_box[0], "author" : row_box[1], "rating": row_box[2], "publisher" : row_box[3], "pages" : row_box[4], "category": row_box[5], "language" : row_box[6]}]
                book_dictionary.update({"Investing" : investing_list})
        
    return book_dictionary