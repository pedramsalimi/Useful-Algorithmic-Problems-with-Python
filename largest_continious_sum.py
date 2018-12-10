class LargestSum(object):

    def __init__(self):

        print("This class provide a methods for finding largest continious sum")

    def first_method(self,l):

        if len(l) == 0:
            return 0
        max_sum = current_sum = l[0]

        for num in l[1:]:

            current_sum = max(current_sum+num, num)

            max_sum = max(max_sum, current_sum)

        return max_sum

l = [1,2,4,6,-2,10,10,-5,3]
obj = LargestSum()
print(obj.first_method(l))
