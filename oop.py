
#面向过程
# std1={'name':mi,'score':98}
# std2={'name':slmao,'score':81}

# def print_score(std):
# 	print('%s:%s'%(std['name'],std[1]))

# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self, name,score,gender):
# 		 self.name=name
# 		 self.score=score
# 		 self.__gender=gender

# 	def print_score(self):
# 		print('%s:%s'%(self.name,self.score))

# 	def get_grade(self):
# 		if self.score>=90:
# 			return 'A'
# 		elif self.score>=60:
# 			return 'B'
# 		else:
# 			return 'C'

# 	def get_gender(self):
# 		return self.__gender

# 	def set_gender(self,gender):
# 		if 0<=gender<=100:
# 		    self.__gender=gender
# 		else:
# 			raise ValueError('bad score')


# bart=Student('slmao',99,55)
# bart.print_score()
# print(bart.name,bart.get_grade())
# print(bart.get_gender())
# bart.__gender=66
# print(bart.__gender)
# print(bart.get_gender())
# bart.set_gender(88)
# print(bart.get_gender())


# class  Animal(object):
	 
# 	def run(self):

# 	 	print('animal is run...')

# class Dog(Animal):

# 	def run(self):

# 	 	print('dog is run...')

# class Cat(object):#不继承有run方法也可以调用
# 	def run(self):
# 		print('cat is run...')
		


# a=Animal()
# a.run()
# d=Dog()
# d.run()

# def run_two(animal):
# 	animal.run()

# run_two(Cat())


# class Student(object):
# 	"""docstring for Student"""

# 	count=0#类属性

# 	def __init__(self, name):
# 		self.name=name
# 		Student.count=Student.count+1
		

# # 测试:
# if Student.count != 0:
#     print('测试失败!1')
# else:
#     bart = Student('Bart')
#     print(bart.count)
#     if Student.count != 1:
#         print('测试失败!2')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!3')
#         else:
#             print('Students:', lisa.count)
#             print('测试通过!')


# def set_score(self,score):
# 	self.score=score

# class Student(object):
# 	#__slots__=('name','age')# 用tuple定义允许绑定的属性名称

# Student.set_score=set_score#加到类上的方法 所有实例都可以用

# s=Student()
# s.name='slmao'
# print(s.name)
# s2=Student()

# def set_age(self,age):
# 	self.age=age

# from types import MethodType
# s.set_age=MethodType(set_age,s)#加到实例上的方法只有当前实例可用
# s.set_age(32)
# print(s.age)
# # s2.set_age(33)
# # print(s2.age)



# s.set_score(99)
# s2.set_score(88)
# print(s.score,s2.score)

# class Screen(object):

# 	def __init__(self):
# 		self._resolution=786432
	
# 	@property
# 	def width(self):
# 		return self._width

# 	@width.setter
# 	def width(self,value):
# 		self._width=value

# 	@property
# 	def height(self):
# 		return self._height
		
# 	@width.setter
# 	def height(self,value):
# 		self._height=value

# 	@property
# 	def resolution(self):
# 		return self._resolution

# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

from enum import Enum,unique

@unique
class Gender(Enum):
	Male=0
	Female=1

class Student(object):
	"""docstring for Student"""
	def __init__(self, name,gender):
		self.name = name
		self.gender=gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
		
		
		