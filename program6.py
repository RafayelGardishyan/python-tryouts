# -*- coding: utf-8 -*-

# Փոփոխական, variable
x = 10
y = 99

# *************************************************************************************************************
# ************************************ Ֆունկցիաների նկարագրություն ********************************************
# *************************************************************************************************************


# Ֆունկցիիա, function
def sum(a, b):
    """Sum. Գումարում։

    Returns a sum of two numbers, a + b

    :param a: Variable. Փոփոխական։
    :param b: Variable. Փոփոխական։
    :return: Result
    """
    return a + b


# Ֆունկցիիա, function
def mult(a, b):
    """Multiplication. Բազմապատկում։

    :param a: Variable. Փոփոխական։
    :param b: Variable. Փոփոխական։
    :return:
    """
    return a * b


def div(a, b):
    """Division.

    :param a:Variable
    :param b:Variable
    :return:
    """
    return(a / b)



# *************************************************************************************************************
# ********************************* Ինչպես են կանչում ֆունկցիաները ********************************************
# *************************************************************************************************************

# Կանչել sum ֆունկցիան 1 և 2 արժեքներով
print sum(1, 2)

# Կանչել sum ֆունկցիան 3 և 85 արժեքներով
print sum(3, 85)

# Կանչել sum ֆունկցիան x և y արժեքներով
print sum(x, y)

# print sum(sum(10, 5), sum(50, 40))

# Կանչել mult ֆունկցիան 13 և 3 արժեքներով
print mult(13, 3)

print mult(26, 10)

print div(39, 3)

# *************************************************************************************************************
# *************************************************************************************************************
# *************************************************************************************************************
m = sum(4, 5)
# m = 4 + 5

n = sum(6, 7)

print mult(m, n)


# sum(1, 2) + mult(3, 4)

