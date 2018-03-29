import random


def main():
	#testlist = random.sample(xrange(1,101), 100)
	testlist = [4,3,10,2,8]
	# testlist[30] = testlist[2]
	# testlist[60] = testlist[2]
	# testlist[90] = testlist[2]
	# testlist[55] = testlist[2]

	print(testlist)
	print(len(testlist))
	print(sum(testlist))

	print(answer(testlist, 12))

	# return [num for num in data if num not in to_delete]


	# [element for element in list_of_dictionaries if element[key] == value]

def answer(l, t):

	#improve worst case efficiency, remove any numbers bigger than t
	# to_delete = set()
	# for num in l:
	# 	if num > t:
	# 		to_delete.add(num)
	# l = [num for num in l if num not in to_delete]
	# finallist = []
	finalstart = -1
	finalend = -1


	if sum(l) < t:
		return [-1, -1]

	print("Passed")
	for start in range(0,len(l)):
		end = start
		while (sum(l[start:end]) < t) and end <= len(l):
			end = end + 1
		if sum(l[start:end]) > t:
			print("Continuing")
			continue
		else:
			finallist = l[start:end]
			finalstart = start
			finalend = end
			break


	if len(finallist) == 0 or sum(finallist) != t:
		finallist = [-1, -1]



	return [finalstart,finalend]



if __name__ == "__main__":
	main()