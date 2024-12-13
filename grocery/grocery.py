def main():
    dict_item = {}
    try:
        try:
            while True:
                item = input("").upper()
                if item in dict_item: dict_item[item] += 1
                else: dict_item[item] = 1
        except KeyError:
            pass
    except EOFError:
        pass


    dict_item = dict(sorted(dict_item.items()))

    for item in dict_item:
        print(f"{dict_item[item]} {item}")


main()
