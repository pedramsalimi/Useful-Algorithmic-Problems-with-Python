class PairSum(object):

    def __init__(self):

        print("This class provide two method for finding pair sums")

    def first_method(self, arrayList, pairValue):
        # simple method
        if len(arrayList) < 2:
            return
        pair_list = []
        for i in arrayList:
            for j in arrayList:
                if i+j == pairValue:
                    element = (i,j)
                    if not (j,i) in pair_list:
                        pair_list.append(element)
                continue
        return pair_list


    def second_method(self, arrayList, pairValue):
        #Advanced method with lower time complexity with just one loop  
        if len(arrayList) < 2:
            return

        seen = set()
        output = set()

        for num in arrayList:

            target = kvalue - num
            if target not in seen:
                seen.add(num)
            else:
                output.add( ((min(num,target)), max(num,target)) )
        print('\n'.join(map(str,list(output))))


arr = [1,2,4,3,3]
kvalue = 6
obj = PairSum()
print(obj.first_method(arr, kvalue))
print(obj.second_method(arr, kvalue))
