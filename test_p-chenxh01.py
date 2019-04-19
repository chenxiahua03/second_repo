height = 1.75
weight = 80.5
bmi = float(weight/height/height)
print(bmi)
# b = int(bmi)
if bmi < 18.5:
    print('过轻:bmi = %.3f' % bmi)
elif 18.5 <= bmi < 25:
    print('正常:bmi = %.3f' % bmi)
elif 25 <= bmi < 28:
    print('过重:bmi = %.3f' % bmi)
elif 28 <= bmi < 32:
    print('肥胖:bmi = %.3f' % bmi)
elif 32 <= bmi < 45:
    print('严重过胖:bmi = %.3f' % bmi)
else:
    print('该减肥了:bmi = %.3f' % bmi)

