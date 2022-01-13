# vrni vrednost

slovar1 = input()
slovar1 = eval(slovar1)

for operacija in slovar1:
    if operacija == "+":
        a = slovar1["+"]
        print(a[0] + int(a[1]))
    elif operacija == "-":
        pass
    elif operacija == "*":
        pass
    elif operacija == "/":
        pass

