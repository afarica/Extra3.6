# Напишите функцию которая подсчитает количество счетных и несчетных чисел в списке
# чисел.
a=int(input("Enter your number:"))
i=0
c=0
while i<=a or c<=a: 
	if i%2==0:
		print(i,'is even')
	elif c%2!=0:
		print(c,'is odd')
	i += 1
	c += 1
