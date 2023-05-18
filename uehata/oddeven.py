def check_odd_even(num:int) -> None:
    if num % 2 == 0:
        print("偶数", end="")
    else:
        print("奇数", end="")

if __name__ == "__main__":
    import sys
    num = int(sys.argv[1])
    check_odd_even(num)