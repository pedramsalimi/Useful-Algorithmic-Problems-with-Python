import collections
class FindMissingValue(object):

    def __init__(self):

        print("This class provide four method for finding missing value that missed from second shuffled list")

    #Simple but high cost method - o(n^2)
    def first_method(self,l1,l2):

        pairlist = []
        target = None
        for i in l1:
            for j in l2:
                if i in l2:
                    pairlist.append(i)
                else:
                    target = i
        return target
    #optimized method - o(NlogN)
    def second_method(self,l1,l2):

        l1.sort()
        l2.sort()

        for i, j in zip(l1,l2):
            if i != j:
                return i
        return l1[-1]
    #another method with 0(NlogN) order with python collections
    def third_method(self,l1,l2):

        d = collections.defaultdict(int)

        for i in l2:
            d[i] += 1
        for i in l1:
            if d[i] == 0:
                return i
            else:
                d[i] -= 1

    #tricky method using XOR
    def fourth_method(self,l1,l2):

        result = 0
        for i in l1+l2:
            result ^= i

        return result



l1 = [1,2,3,4,5]
l2 = [4,2,1,5]
finder = FindMissingValue()
print(finder.first_method(l1,l2))
print(finder.second_method(l1,l2))
print(finder.third_method(l1,l2))
print(finder.fourth_method(l1,l2))
