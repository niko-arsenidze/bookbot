def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    #Calculate number of words
    number_of_words = count_words(text)
    print(f"This book has {number_of_words} words.")
    
    #Calculate number of character occurances & sort them by amount
    character_count = count_characters(text)
    list_of_dicts = convert_dict(character_count)
    sorted_dicts = sort_dict(list_of_dicts)
    
    #Generate message and print it to the console
    character_message(sorted_dicts)
    





def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def count_characters(text):
    lowercase = text.lower()
    character_count = {}
    for c in lowercase:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count
        #print(character_count)

def convert_dict(dict):
    list_of_dicts = []
    for key in dict:
        if key.isalpha():
            small_dict = {"char" : key, "amount" : dict[key]}
            list_of_dicts.append(small_dict)
    return list_of_dicts


def sort_dict(list_of_dicts):
    def sort_on(dict_item):
        return dict_item["amount"]

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


def character_message(sorted_list):
    for dict in sorted_list:
        print(f"The {dict["char"]} character was found {dict["amount"]} times")



main()

