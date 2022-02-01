### Question for Bill. ### Can a splat variable be named a singluar? Or does it always need to be plural?
### Also what is up with the learning platform code? Explain figuring it out with Dimitri and the rediculousness of having multiple variables of the same name. 

# class MathDojo:
#     def __init__(self):
#     	self.result = 0
#     def add(self, num, *nums):
#     	# your code here
#     def subtract(self, num, *nums):
#     	# your code here
# # create an instance:
# md = MathDojo()
# # to test:
# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)	# should print 5
# # run each of the methods a few more times and check the result!


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
x.add(2,3,3).add(2,3,3).sub(5,5,5).add(5,4,3,2,1).sub(5,5,5,5).sub(-5)
# print(MathDojo().add_second_method(2,3,3,5))
# print(MathDojo().add(2,3,3,5))

# def add(self, num, *nums):
#         for  i in (nums):
#             if num in nums:
#                 self.result = (num + nums(i))
#         return self.result

# print(add(2,3))