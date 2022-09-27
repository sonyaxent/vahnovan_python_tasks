# The input is a string of characters separated by spaces.
# Write a program that groups like characters together to form a nested list.
if __name__ == "__main__":

    group_list = []
    for i in input().split():
        if (not group_list) or (i != group_list[-1][-1]):
            group_list.append([i])
        else:
            group_list[-1].append(i)
    print(group_list)