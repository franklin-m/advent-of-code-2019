min_val = 147981
max_val = 691423
counter = 0


def check_val(inp: int, p1: bool):
    # i don't think this would pass all test cases, but for some reason it got the answer
    arr = []
    for integer in str(inp):
        arr.append(int(integer))
    if arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5]:
        if p1:
            if arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[3] or arr[3] == arr[4] or arr[4] == arr[5]:
                return True
        else:
            for i in range(len(arr)):
                if arr.count(arr[i]) == 2:
                    return True
    else:
        return False


for i in range(min_val, max_val): 
    if check_val(i, False):  # change to true for part 1
        counter += 1

print(counter)
