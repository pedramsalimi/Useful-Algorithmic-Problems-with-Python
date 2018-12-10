class SenteceRiversal(object):

    def __init_(self):

        print("this class provides methods for reverse the given sentence")

    # simplest way that is easy to read version of second_tricky method
    def first_method(self,text):

        word_list = text.split()
        word_list = word_list[::-1]
        new_str = ' '.join(word_list)
        return new_str

    def first_tricky(self,text):

        return " ".join(reversed(text.split()))


    def second_tricky(self,text):

        return " ".join(text.split()[::-1])


    def main_method(self,text):

        words = []
        length = len(text)
        spaces = [' ']

        i=0

        while i < length:

            if text[i] not in spaces:

                word_start = i

                while i < length and text[i] not in spaces:

                    i += 1

                words.append(text[word_start:i])

            i += 1

        return " ".join(reversed(words))

obj = SenteceRiversal()
text = 'hello undefined floating object'
print(obj.first_method(text))
print(obj.first_tricky(text))
print(obj.second_tricky(text))
print(obj.main_method(text))
