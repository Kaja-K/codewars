""" 
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving 
the even numbers at their original positions.

    [7, 1]  =>  [1, 7]
    [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

"""


def sort_array(source_array):
    solution = []
    sorted_odd = []
    for number in source_array:
        if number % 2 == 0:
            solution.append(number)
        else:
            solution.append("")
            sorted_odd.append(number)
    sorted_odd.sort()
    for i in range(len(solution)):
        if solution[i] == "":
            solution[i] = sorted_odd.pop(0)
    return solution
