# Anagram Checking

class Anagram(object):

    def __init__(self):
        print("You can use this class to Check Anagrams with 3 methods")


    def with_space(self, s1, s2):

        s1 = ''.join(sorted(str1.lower()))
        s2 = ''.join(sorted(str2.lower()))
        return s1 == s2

    def without_space(self, s1, s2):

        s1 = s1.replace(' ', '').lower()
        s2 = s2.replace(' ', '').lower()

        return sorted(s1) == sorted(s2)

    def dictionary_way(self, s1, s2):

        s1 = s1.replace(' ', '').lower()
        s2 = s2.replace(' ', '').lower()

        if len(s1) != len(s2):
            return False

        count = {}

        for letter in s1:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        for letter in s2:
            if letter in count:
                if letter in count:
                    count[letter] -= 1
                else:
                    count[letter] = 1
        for k in count:
            if count[k] != 0:
                return False
        return True


str1 = "Hello Buddy"
str2 = "olleh dduby"
a = Anagram()
print(a.with_space(str1,str2))
print(a.without_space(str1,str2))
print(a.dictionary_way(str1,str2))
