# Steps to do calculations:

# Take number as a string, sort it to ascending and descending order
# convert both to decimal (base 10) and do the subtraction
# convert back to original base

# converting from base b to int:
# int('num', b)

# converting from int to base b:
# 	num = __
# 	s=""
# 	while num:
# 		s.append(int(num % b))
# 		num = num / b
# 	s is now the base number

def DecToBase(n, b):
	print("Entered DecToBase")
	if n < 0:
		n = n * -1
	num = n 
	digits = []
	while num:
		#print(num)
		digits.append(str(int(num % b)))
		num = num / b
	digits.reverse()
	print("Digits = " + str(digits))
	return ''.join(digits)

def BaseToDec(n, b):
	print("Entered BaseToDec")
	if b != 10:
		return int(n, b)
	else: 
		return int(n)

def answer(n, b):
	k = len(n)
	currentnum = n
	count = 0
	result_list = []
	string_match = ''
	matchfound = False
	# while third_matchfound == False:
	while matchfound == False:
		y = ''.join(sorted(currentnum))
		x = y[::-1]
		print(x,y)

		int_x = BaseToDec(x, b)
		int_y = BaseToDec(y, b)

		print(int_x, int_y)

		int_z = int_x - int_y
		print("Int_z = " + str(int_z))
		newnum = DecToBase(int_z, b)
		if len(newnum) < k:
			newnum = '0' + newnum
		# if newnum in result_list:
		# 	if second_matchfound == False:
		# 		second_matchfound = True
		# 		string_match = newnum
		# 		result_list.append(newnum)
		# 		second_match_index = len(result_list)
		# 	elif second_matchfound == True and newnum == string_match:
		# 		third_matchfound = True
		# 		result_list.append(newnum)
		# 		third_match_index = len(result_list)
		# else:
		# 	string_match = ''
		# 	result_list.append(newnum)
		if newnum in result_list:
			matchfound = True
			for i in range(0, len(result_list)):
				if newnum == result_list[i]:
					matchindex = i
					break
			result_list.append(newnum)
		else:
			result_list.append(newnum)
			currentnum = newnum
			count = count + 1
	print("result_list: " + str(result_list))

	cycle_list = result_list[matchindex:-1]
	print("cycle_list: "+ str(cycle_list))




	return len(cycle_list)





def main():
	number = "210022"
	print("Final return: " + str(answer(number, 3)))


if __name__ == "__main__":
	main()



# Google invite code: https://goo.gl/zc37Rn