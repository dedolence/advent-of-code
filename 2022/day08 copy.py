var = 0
lst = ["foo", "bar"]
str = "baz"


def do_some_stuff(i):
    return True


def main():
    global var
    print(str)
    print(lst)
    for i in lst:
        var += 1

if __name__ == "__main__":
    main()