def find_max_min(data):

    min_max = []
    max_num = max(data)
    min_num = min(data)


    if isinstance(data, list):
        if max_num == min_num:
            min_max.append(max_num)
            return min_max
        else:
            min_max.append(min_num)
            min_max.append(max_num)
            return min_max
    else:
        return None

data = [67,4,67,2,34,10]
print(find_max_min(data))