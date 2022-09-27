
def func_depth(height_list):
    right_side_list = []
    left_side_list = []
    for _ in reversed(height_list):

        if _ > min(height_list):
            right_side_list.append(_)
        else:
            break

    right_side = max(right_side_list) - min(height_list)

    for i in height_list:
        if i > min(height_list):
            left_side_list.append(i)
        else:
            break

    left_side = max(left_side_list) - min(height_list)

    return min(left_side, right_side)

mountain = [3000, 1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2, 2000]

if __name__ == "__main__":
    print(func_depth(mountain))


