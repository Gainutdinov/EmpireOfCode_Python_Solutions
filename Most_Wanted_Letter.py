from collections import Counter
import re

def most_letter(text, all_letters=False):
    text = re.sub('[^a-zA-Z0-9\.]', '', text)
    text = text.lower()
    print(text)
    c = Counter(text)
    # replace this for solution
    print((list(c.most_common())[0])[0])
    return 0


most_letter("Lorem ipsum dolor sit amet")
