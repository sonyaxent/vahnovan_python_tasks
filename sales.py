# Write a program that counts the number of items purchased by customers in an online store.
# The input to the program is the number n -
# the number of purchase records, and then n lines of the form "Buyer Product Quantity".
# For each customer, the program should display a list of purchases.
if __name__ == "__main__":

	sales = {}
	for _ in range(int(input())):
		name, item, count = input().split()
		sales[name][item] = sales.setdefault(name, {}).setdefault(item, 0) + int(count)
	for key in sorted(sales):
		print(f'{key}:')
		for i in sorted(sales[key].items()):
			print(*i)