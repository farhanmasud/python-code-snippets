import re


def count_from_string(string):
    """Takes a string and returns word count"""
    # replace all extra whitespace
    string = re.sub("\s{2,}", " ", string)
    # consider as a word only if it contains a letter or a number
    count = len(
        [
            word
            for word in string.split(" ")
            if any(c.isalpha() or c.isnumeric() for c in word)
        ]
    )

    return count


def count_from_txt_file(file_path):
    """Takes a txt file and returns word count"""
    if file_path.endswith(".txt"):
        with open(file_path, "r") as text_file:
            count = count_from_string(text_file.read())
            return count

    else:
        print("Please pass file path of txt format")
