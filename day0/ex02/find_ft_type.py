
def print_type(string: str, object: any):
  print(f"{string} : {type(object)}")

def all_thing_is_obj(object: any) -> int:
  match object:
    case list():
      print_type("List", object)
    case tuple():
      print_type("Tuple", object)
    case set():
      print_type("Set", object)
    case dict():
      print_type("Dict", object)
    case str():
      print_type(f"{object} is in the kitchen", object)
    case _:
      print("Type not found")

  return 42
