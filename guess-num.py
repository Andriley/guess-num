import random

r = random.randint(1,100)
while True:
	num = input('please guess the num: ')
	num = int(num)
	if num == r:
		print('correct answer!')
		break
	else:
		if num > r:
			print(num,'is bigger than the answer')
		else:
			print(num, 'is smaller than the answer')