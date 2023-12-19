# For encoding if the length of the word < 3, just reverse it else take the 1st character and add it at the back and add 3 random characters to both front and back
# For decoding if the length of the word < 3, just reverse it else remove 3 characters from front and back then move last character and add it to the front

import random
import string
coding = int(input("1 for Encoding and 0 for Decoding: "))
msg = input("Enter the message: ")
words = msg.split(" ")
if(coding):
    nstr = []
    for word in words:
        if len(word) >= 3:
            r1 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            r2 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            # string.ascii_letters ->contains all the ASCII letters
            # random.choice(string.ascii_letters) -> randomly select a character from the set of letters.
            nwords = r1 + word[1:] + word[0] + r2
            nstr.append(nwords)
        else:
            nstr.append(word[::-1])
    print(" ".join(nstr))
else :
    nstr = []
    for word in words:
        if len(word) >= 3:
            nword = word[3:-3]
            nword = nword[-1] + nword[:-1]
            nstr.append(nword)
        else :
            nstr.append(word[::-1])
    print(" ".join(nstr))