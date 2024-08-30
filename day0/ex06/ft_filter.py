def ft_filter(func, iterable):
    iterable_filtered = [item for item in iterable if func(item)]
    return iter(iterable_filtered)


if __name__ == "__main__":
    filter(None, 2)
