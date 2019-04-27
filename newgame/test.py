print("今有物：")
none = True
number = 0
while none:
    number += 1
    if number%3 == 2 and number%5 == 3 and number%7 == 2:
        print("答曰：",number)
        none = False