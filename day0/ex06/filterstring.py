def ft_filter

if __name__ == "__main__":
    print(f"Hello {__file__.split('.')[0]}!")
    print(filter.__doc__)
    # print(help(filter))

    ages = [5, 12, 17, 18, 24, 32]

    test = filter(ages)

    for x in test:
        print(x)
