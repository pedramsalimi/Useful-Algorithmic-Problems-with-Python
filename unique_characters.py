
class Unique_chars(object):

    def __init__(self):

        print("'This functions return's True if all character in a string are unique:\
        'abcde' -> True      but     'aabcde' -> False'")

    def first_unique_chars(self,s):

        return len(s) == len(set(s))

    def second_unique_chars(self,s):

        chars = set()

        for let in s:
            if let in chars:
                return False
            else:
                chars.add(let)
        return True


obj = Unique_chars()
a = 'aabcde'
b = 'abcde'
print(obj.first_unique_chars(a))
print(obj.second_unique_chars(a))
print(obj.first_unique_chars(b))
print(obj.second_unique_chars(b))
