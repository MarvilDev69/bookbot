def count_words(contents_book):  
    words = contents_book.split()
    return len(words)

def number_of_characters(contents_book):
    lower_case = contents_book.lower()
    char_list = list(lower_case)
    char_dict = {}
    for char in char_list:
        if char.isalpha() == True:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sorting(print_list_dict_count):
    sorted_dict = dict(sorted(print_list_dict_count.items(),key=lambda x: x[1], reverse=True))

    return sorted_dict

    
    