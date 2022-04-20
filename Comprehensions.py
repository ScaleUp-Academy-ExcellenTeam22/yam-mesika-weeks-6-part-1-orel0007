import re


def words_length(sentence):
    """
    Create list Comprehension in len of words in the sentence.
    :param sentence:String of words.
    :return: List lens of word in tne given sentence.
    """
    return[len(word) for word in sentence.split()]


def get_letters():
    """
    Create list Comprehension of all letters a-z and A-Z
    :return:List with letter a-z and A-Z
    """
    return [chr(letter) for letter in range(ord('a'), ord('z'))] + [chr(letter) for letter in range(ord('A'), ord('Z'))]


def count_words(txt):
    """
    Create dictionary Comprehension of words and the length of words while contain only letters a-z and A-Z.
    :param txt: string of sentences
    :return: dictionary when key is the word and value is the length of word.
    """
    words_list = [re.sub(r'[^a-zA-Z]', '', word) for word in txt.split(" ")]
    return {word: len(word) for word in words_list}


def full_names(names, family_names, min_length=-1):
    """
    Create new list of names when combine each first names and last names, in condition if min_length given is bigger
     than 0 insert only names with length bigger than min_length.
    :param names: first names list
    :param family_names: last names list
    :param min_length: insert names
    :return: list of names
    """
    return list(filter(lambda name: True if len(name) < 0 or len(name) > min_length else False,
                       [(f_name + " " + l_name).capitalize() for f_name in names for l_name in family_names]))


if __name__ == "__main__":
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
    print(get_letters())
    text = """You see2, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names, min_length=0))
    print(full_names(first_names, last_names, min_length=10))
