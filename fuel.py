x, y = input("Fraction: ").split("/")


try:
    percentage = round(int(x) / int(y) * 100)

    if percentage > 100:
        pass
    elif percentage  <= 1 :
        print("E")
    elif percentage >= 99:
       print("F")
    else:
        print(percentage, "%")

except ValueError:
    print ("ValueError")
except ZeroDivisionError:
    print ("Zero Error")

