To contact the project:
   Email: leenaford@cmail.carleton.ca
   
Date: 09/04/2022
Software Name: A Data Analyzer User Interface
Version: 1.0
   
## Description
The project involves a user interface which prompts the user to enter any command from a list of commands. Depending on the user's input, the program will load a book dataset formatted as a CSV file and search through the set, add/remove a book to the set, retrieve a specific piece of data, or sort the dataset in a particular manner. Upon returning the desired outcome, the program will re-display a list of commands to the user.

The project is made up of four files:
- T051_P4_booksUI.py  (A Python file involving functions written to develop the user interface, and importing from modules containing the data analyzing functions)
- T051_P2_add_remove_search_dataset.py (A Python file involving the adding/removing/searching functions used to analyze the book dataset)
- T051_P3_sorting_fun.py (A Python file involving the soring functions used to analyze the book dataset)
- T051_P5_load_data.py (A Python file involving the function that reads the CSV dataset and organizes the file as a book category dictionary where the keys are the categories and the values are a list of books in that category)

## Installation
You **must** have at least Python 3.7.4 installed or a later version to use the program. The main program is found in the file T051_P4_booksUI.py, however to use the program you must also load the following modules:
- T051_P5_load_data.py
- T051_P2_add_remove_search_dataset.py
- T051_P3_sorting_fun.py. 

You must use save your book dataset (as a CSV file) in the same directory containing all the files used for this project.

## Usage
> python T051_P4_booksUI.py

After being prompted to do so, enter a command from the list of commands displayed. If you do not type the load command first, you will be prompted to load the data before using inputting any other command in the program. There is no error control if you type in the wrong data set file (therefore make sure you are typing the data filename correctly). Follow the commands to analyze the dataset to your preference or quit the program.
## Credits
- T051_P5_load_data.py: Originally written by Umayer Joarder, and modified to take care of duplicate books by Espen Swift.
- T051_P2_add_remove_search_dataset.py: 

| Function | Author |
| ------ | ------ |
| add_book | Isabella Fotia |
| remove_book | Isabella Fotia |
| get_books_by_category | Umayer Joarder |
| get_books_by_rate | Espen Swift |
| get_books_by_title | Leena Ford |
| get_books_by_author | Espen Swift |
| get_books_by_publisher | Umayer Joarder |
| get_all_categories_for_book_title | Leena Ford |
  
- T051_P2_sorting_fun.py:

| Function | Author |
| ------ | ------ |
| dictionary_to_list | Espen Swift |
| sort_books_title | Leena Ford |
| sort_books_publisher | Umayer Joarder |
| sort_books_author | Espen Swift |
| sort_books_ascending_rate | Isabella Fotia |

- T051_P4_booksUI.py

| Commands | Author |
| ------ | ------ |
| commands for add_book, remove_book | Isabella Fotia |
| commands for get_books_by_title/rate/author | Leena Ford |
| commands for get_books_by_publisher/category and get_all_categories_for_book_title | Umayer Joarder |
| commands for sort_books_title/author/publisher/ascending_rate | Espen Swift |

   - Refactoring functions in the user interface:
      - display_menu function: written by Leena Ford
      - adding function: written by Leena Ford
      - removing function: written by Leena Ford
      - get_functions function: written by Leena Ford
      - sort_functions function: written by Leena Ford
      - after_loading function: written by Leena Ford
      - if_loaded function: written by Leena Ford
 

## License

Copyright (c) 2022 Leena Ford, Espen Swift, Isabella Fotia, Umayer Joarder
[![License](https://img.shields.io/badge/License-BSD_2--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
