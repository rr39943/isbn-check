def isbn_check(number):
    isbn = number.replace("-", "")
    isbn = list(isbn)

    # turn X into 10
    if isbn[-1] == "x" or isbn[-1] == "X":
        isbn[-1] = "0"

    # check if only digit
    for i in isbn:
        if i.isdigit():
            pass
        else:
            print("Incorrect ISBN. (Letters instead of numbers)")  # or return False
            return False

    # check if 10 or 13
    if len(isbn) == 10:
        sum_check = int(isbn[0]) * 10 + int(isbn[1]) * 9 + int(isbn[2]) * 8 + \
                    int(isbn[3]) * 7 + int(isbn[4]) * 6 + int(isbn[5]) * 5 + int(isbn[6]) * 4 + \
                    int(isbn[7]) * 3 + int(isbn[8]) * 2 + int(isbn[9]) * 1
        if sum_check % 11 == 0:
            print ("Correct ISBN.")  # or return True
        else:
            print ("Incorrect ISBN.")  # or return False
    elif len(isbn) == 13:
        sum_check = int(isbn[0]) * 1 + int(isbn[1]) * 3 + int(isbn[2]) * 1 + int(isbn[3]) * 3 + int(
            isbn[4]) * 1 + int(isbn[5]) * 3 + int(isbn[6]) * 1 + int(isbn[7]) * 3 + int(
            isbn[8]) * 1 + int(isbn[9]) * 3 + int(isbn[10]) * 1 + int(isbn[11]) * 3 + int(
            isbn[12]) * 1
        if sum_check % 10 == 0:
            print("Correct ISBN.")  # or return True
        else:
            print ("Incorrect ISBN.")  # or return False
    else:
        print ("Incorrect ISBN. (Wrong length)")



# DEBUG tests
isbn_check("978-88-459-1152-X")
