class MirrorStringCheck(object):

    def __init__(self):

        print('This class provide a method to check if given string contain\
        mirrored element or not; for example:\
        "aabbaa" is mirrored but "aabba" is not')

    def mirrorChecker(self,s):

        myStringList = list(s)
        for i in range(0, int(len(myStringList)/2)):
            if myStringList.pop(0) == myStringList.pop(-1):
                continue
            return False
        return True


s = 'aabbaa'
obj = MirrorStringCheck()
print(obj.mirrorChecker(s))
