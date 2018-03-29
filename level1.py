# a = [[0 for x in range(10)] for y in range(2)]

# a[0][5] = 12

# print(a)







# [element for element in list_of_dictionaries if element[key] == value]



def main():
	data = [1,2,2,3,3,3,3,4,5,5]
	n =0
	print(answer(data,n))




def answer(data, n):
	print("Entered")
	numtrack = {}

	for num in data:

		if num in numtrack:
			numtrack[num] = numtrack[num] + 1
		else
:			numtrack[num] = 1

	to_delete = set()
	for num, count in numtrack.items():
		if count > n:
			to_delete.add(num)


	return [num for num in data if num not in to_delete]


if __name__ == "__main__":
    main()