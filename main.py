def main():

    book_path = "books/frankenstein.txt"
    text = read_text(book_path)
    lowered_string = text.lower()

    words_in_data = count_words(text)
    characters_in_data = count_characters(lowered_string)


#    print(f"{characters_in_data} characters are found in the document.")

    print(f"-- Begin report of {book_path} --")
    print(f"{words_in_data} words are found in the document.")
    print(" ")
    counter_print(characters_in_data)# print the counter
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)


def read_text(path):
    with open(path) as f:
        return f.read()


def count_characters(lowered_string):
    characters_dict = {}
    #add every letter to a dictionary where the letter increases
    for character in lowered_string:
        if character.isalpha():
            if character in characters_dict:
                characters_dict[character] += 1
            else:
                characters_dict[character] = 1

    #convert to list
    letters_list = []
    for letter, count in characters_dict.items():
        letters_list.append({"letter": letter, "count": count})
    
    letters_list.sort(reverse=True, key=sort_on)
    
    return letters_list

def sort_on(characters_in_data):
    return characters_in_data["count"]

#print every letter with the count
def counter_print(characters_in_data):
    
    for character in characters_in_data:
        print(f"The {character['letter']} character was found {character['count']} times")



main()