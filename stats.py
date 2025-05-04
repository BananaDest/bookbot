def get_number_of_words(string):
    return len(string.split())

def count_characters(book):
    book_lower = book.lower() 
    char_count = {char: book_lower.count(char) for char in set(book_lower)}
    return char_count

def sorted_list_of_dictionaries(book_dict):
    list_of_dicts =  [{"char": key, "value":value } for key, value in book_dict.items()]
    list_of_dicts.sort(reverse=True,key=lambda d: d["value"])
    return list_of_dicts
