import re

def main():
    lst_month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


    try:
        while True:
            strinput = input("Date: ").strip()
            str = ""
            month = ""
            day = ""
            year = ""

            if " " in strinput and not("," in strinput) and not("/" in strinput): continue
            else: str = re.split(r"[ ,/]+",strinput)

            if not (str[1].isalpha()) and not (str[2].isalpha()):
                day = "{:02}".format(int(str[1]))
                year = str[2]
            else: continue

            if str[0].title() in lst_month:
                if "/" in strinput and not(" " in strinput) and not("," in strinput): continue
                else: month = int(lst_month.index(str[0].title()))+1
            elif not (str[0].isalpha()):
                month = "{:02}".format(int(str[0]))
            else: continue

            if len(str)==3:
                if len(year)==4 and 1<= int(month) <=12 and 1<= int(day) <=31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else: continue
            else: continue
    except (EOFError):
        pass

main()
