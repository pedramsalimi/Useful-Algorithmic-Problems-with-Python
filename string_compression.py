class StringCompression(object):

    def __init__(self):

        print("This class provide  a method for string compression\
        Example:\
        'AAAABBBBCCCC' -> 'A4B4C4' ; methods are also case sensitive\
        'AAaa' -> 'A2a2'")

    def compress(self,s):

        r = ''
        l = len(s)

        if l == 0:
            return ''

        if l == 1:
            return s+'1'

        last = s[0]
        count = 1
        i = 1

        while i < l:

            if s[i] == s[i-1]:
                count += 1
            else:
                r = r + s[i-1] + str(count)
                count = 1
            i += 1


        r = r + s[i-1] + str(count)

        return r

s = 'AAAABBBB'
s1 = 'AAAaaa'
s2 = 'aAbB'
obj = StringCompression()
print(obj.compress(s))
print(obj.compress(s1))
print(obj.compress(s2))
