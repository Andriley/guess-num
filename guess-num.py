import random

r = random.randint(1,100)
t = 0
while True:
	num = input('please guess the num: ')
	num = int(num)
	if num == r:
		print('correct answer!')
		t = t + 1
		break
	else:
		if num > r:
			print(num,'is bigger than the answer')
			t = t + 1
		else:
		 	print(num, 'is smaller than the answer')
		 	t = t + 1
print('you have tried', t, 'times')