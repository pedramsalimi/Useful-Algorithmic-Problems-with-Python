class BalancedParanthesesCheck(object):

    def __init__(self):

        print('This class provide a method for checking if a given string\
        that contains different kinf of parentheses are matched togheter\
        or not; for example:\
        "{[]}"-> True while "{[}}"> False')

    def balance_check(self,s):

        if len(s) % 2 != 0:
            return False

        opening = set('([{')
        matches = set([('(',')'),('[',']'),('{','}')])
        stack = []

        for parentheses in opening:

            if parentheses in opening:
                stack.append(parentheses)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()

                if(last_open,parentheses) not in matches:
                    return False
        return len(stack) == 0


s1 = '[]'
s2 = '[](){[()]}'
s3 = '[{(]}]'

obj = BalancedParanthesesCheck()
print(obj.balance_check(s1))
print(obj.balance_check(s2))
print(obj.balance_check(s3))
