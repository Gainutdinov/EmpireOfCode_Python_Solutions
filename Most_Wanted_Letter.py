from collections import Counter
import re


def most_letter(text, all_letters=False):
    text = re.sub('[^a-zA-Z\.]', '', text)
    text = text.lower()
    c = Counter(text)
    fir_letter = list(c.most_common())[0]
    if all_letters == False:
        equal_val_list = []
        # add first common letter into the list
        equal_val_list += fir_letter[0]
        if len(c) != 1:
            for value, count in c.most_common():
                # count equal to number of the counts of the most_common letter then add it to equal_val_list
                if count == (list(c.most_common())[1])[1]:
                    equal_val_list += value
                else:
                    break
            equal_val_list.sort()
            # print(equal_val_list[0])
            return equal_val_list[0]
        else:
            return fir_letter[0]
    else:
        equal_val_str = ""
        temp_list = []
        # print(c.most_common())
        previous_count = fir_letter[1]
        for value, count in c.most_common():
            if count == previous_count:
                temp_list += value
                temp_list.sort()
            elif temp_list == []:
                equal_val_str += value
            else:
                equal_val_str += ''.join(temp_list)
                temp_list = []
                temp_list += value
            previous_count = count
        if temp_list:
            equal_val_str += ''.join(temp_list)
        #print(equal_val_str)
        return equal_val_str

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank_1
    assert most_letter("Hello World!") == "l", "Hello test"
    assert most_letter("How do you do?") == "o", "O is most wanted"
    result = most_letter("One")
    assert len(result) == 1 and result in "one", "All letter only once."
    assert most_letter("Oops!") == "o", "Don't forget about lower case."
    result = most_letter("AAaooo!!!!")
    assert len(result) == 1 and result in "ao", "Only letters."
    result = most_letter("abe")
    assert len(result) == 1 and result in "abe", "The First."
    result = most_letter("Lorem ipsum dolor sit amet")
    assert len(result) == 1 and result in "mo", "Lorem 1."

    # Rank_2
    assert most_letter("Lorem ipsum dolor sit amet") == "m", "Lorem 2."
    assert most_letter("One") == "e", "One 2"
    assert most_letter("AAaooo!!!!") == "a", "Only letters. 2"
    assert most_letter("bcdefghijklmnaopqrstuvwxyz") == "a", "ABC"

    # Rank_3
    assert most_letter("Lorem ipsum dolor sit amet", True) == "moeilrstadpu", "Lorem 3."

    print("Use 'Check' to earn sweet rewards!")
