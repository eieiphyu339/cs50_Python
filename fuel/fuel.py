def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    if "/" in fraction:
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator == 0:
            raise ZeroDivisionError("Denominator can't be zero.")
        if numerator>denominator:
            raise ValueError("Numerator cannot be greater than denominator.")
        return round((numerator/denominator)*100)
    else:
        raise ValueError("Invalid fraction format.")

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage<=1:
        return "E"
    else:
        return f"{percentage}%"

# def main():
#     while True:
#         try:
#             str = get_data("Fraction: ")
#             if "/" in str:
#                 lst = str.split("/")
#                 if 99<= round((int(lst[0])/int(lst[1]))*100) <= 100:
#                     print("F")
#                     break
#                 elif 0<= round((int(lst[0])/int(lst[1]))*100) <= 1:
#                     print("E")
#                     break
#                 elif round((int(lst[0])/int(lst[1]))*100)>100:
#                     pass
#                 else:
#                     print(f"{round((int(lst[0])/int(lst[1]))*100)}%")
#                     break
#         except (ValueError, ZeroDivisionError):
#             pass

def get_data(prompt):
    return input(prompt)

if __name__ == "__main__":
    main()
