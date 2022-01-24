### Question for Bill. ### Can a splat variable be named a singluar? Or does it always need to be plural?

class MathDojo:
    def __init__(self):
        self.result=0
    
    def __str__(self):
        return str(self.result)

    def add(self, *nums):   ### Can a splat variable be named a singluar? Or does it always need to be plural?
        for num in (nums):
            self.result += num
        print(self.result)
        return self
    def sub(self, *nums):
        for num in (nums):
            self.result -= num
        print(self.result)
        return self
    # def add(self, num, *nums):
    #     self.result += num
    #     for num in (nums):
    #         self.result += num
    #     return self
x = MathDojo()
x.add(2,3,3).add(2,3,3).sub(5,5,5).add(5,4,3,2,1).sub(5,5,5,5).sub(-5,-5,)
# print(MathDojo().add_second_method(2,3,3,5))
# print(MathDojo().add(2,3,3,5))

# def add(self, num, *nums):
#         for  i in (nums):
#             if num in nums:
#                 self.result = (num + nums(i))
#         return self.result

# print(add(2,3))