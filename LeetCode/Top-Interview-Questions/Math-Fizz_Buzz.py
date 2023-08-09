class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        newList = []
        for i in range(1,n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                newList.append("FizzBuzz")
            elif (i % 5 == 0):
                newList.append("Buzz")
            elif (i % 3 == 0):
                newList.append("Fizz")
            else:
                newList.append(str(i))
        return newList