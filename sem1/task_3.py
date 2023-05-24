number = input("Введите номер билета: ")
a = number[0]
b = number[1]
c = number[2]
d = number[3]
e = number[4]
f = number[5]
if int(a) + int(b) + int(c) == int(d) + int(e) + int(f):
    print("Ваш билет счастливый!")
else:
    print("Вам не повезло, билет не счастливый!")