import sys
from stats import count_words, number_of_characters, sorting

def function(get_book_text):
    with open(get_book_text) as f:
        file_contents = f.read()
    return file_contents

get_book_text = str
contents_book = str
print_count = int
print_list_dict_count = dict
list_sorted = dict
def main(): 
    get_book_text = sys.argv[1]
    contents_book = function(get_book_text)
    print_count = count_words(contents_book)
    print_list_dict_count = number_of_characters(contents_book)
    list_sorted = sorting(print_list_dict_count)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {get_book_text}")
    print("----------- Word Count ----------")
    print(f"Found {print_count} total words")
    print("----------- Character Count ----------")
    for key, value in list_sorted.items():
        print(f"{key}: {value}")
    return
    

main()