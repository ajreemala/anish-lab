class MyMath(object):
    def __init__(self):
        pass
    # returns the max of the list
    def max(self, l):
        mush = 0
        for i in l:
            if i > mush:
                mush = i
        return mush

    def min(self, l):
        mush = None
        for v in l:

            if mush==None or v < mush:
                mush=v
        return mush

    def power(self, base, exponent):
        counter=0
        multiplyer=1
        while counter < exponent:
            multiplyer=base*multiplyer
            counter=counter+1
        return multiplyer

    def mult(self, a, b):
        counter=0
        currentadder = 0
        while counter < b:
            currentadder=currentadder + a
            counter=counter+1
        return currentadder

    def factorial(self, a):
        x=a
        result=1
        if x == 0:
            return 1

        while x != 0:
            result=x*result
            x=x-1
        return result

    def taylor_series(self, n):
        counter = 1
        result = 1/self.factorial(0)
        while counter <= n:
            result = result + 1.0/self.factorial(counter)
            counter = counter + 1
        return float(result)
