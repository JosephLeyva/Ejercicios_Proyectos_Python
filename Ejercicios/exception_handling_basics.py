try:
    i = 0
    j = 10 / i
    values = [1, '1']
    sum(values)
except TypeError:
    print("Type Error")
    j = 10
except ZeroDivisionError as e:
    print("Zero Divison Error")
    print(e)
    j = 0
else:
    print("else")
finally:
    print("Finally")
print(j)
print("End")
