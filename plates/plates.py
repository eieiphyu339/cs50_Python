import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not(2<= len(s) <=6):
        return 0

    if not(s[0].isalpha() and s[1].isalpha()):
        return 0

    if not s.isalnum():
        return 0

    for i, c in enumerate(s):
        if c.isdigit():
            if c == "0":
                return 0

            if not s[i:].isdigit():
                return 0
            break

    return 1

# def is_valid(s):
#     char_part = ""
#     num_part = ""
#     combination = ""
#     for c in s:
#         if (65 <= ord(c) <=90) or (97<= ord(c) <=122): char_part += c
#         if c.isnumeric(): num_part += c

#     if(len(num_part)>0):
#         combination = char_part + str(int(num_part))
#     else:
#         combination = char_part + num_part

#     if(len(char_part)>=2 and len(combination)<=6 and combination==s):
#         return 1
#     else:
#         return 0

if __name__ == "__main__":
    main()
