# python 3.5.2

# This program determines whether a sequence of array elements is an arithmetic progression.

# Counting matches
count = 1


def arifm(obj):
    global count
    for i in range(len(obj)):

        # Firstly check if index < length of list
        if (i + 1) < len(obj):

            # Secondly check if sequence matches with arithmetic sequence
            if ((obj[2] - obj[1]) + obj[i]) == obj[i + 1]:
                count += 1

    if count == len(obj):
        print("This is arifmetic progression.")
    else:
        print("This is not arifmetic progression.")


arifm([1, 2, 3, 4, 5])