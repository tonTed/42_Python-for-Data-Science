def print_type(string: str, object: any):
    print(f"{string}: {object} {type(object)}")


def NULL_not_found(object: any) -> int:

    if object and object == object:
        print("Type not found")
        return 1
    if object is None:
        print_type("Nothing", object)
    elif object is int():
        print_type("Zero", object)
    elif object is str():
        print_type("Empty", object)
    elif object is bool():
        print_type("Fake", object)
    elif object != object:
        print_type("Cheese", object)
    else:
        print("Type not found")
        return 1
    return 0
