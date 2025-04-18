def all_thing_is_obj(object: any) -> int:
    if not isinstance(object, int):
        if isinstance(object, list):
            print("List : ", end="")
        elif isinstance(object, tuple):
            print("Tuple : ", end="")
        elif isinstance(object, set):
            print("Set : ", end="")
        elif isinstance(object, dict):
            print("Dict : ", end="")
        elif isinstance(object, str):
            print(object, "is in the kitchen : ", end="")
        print(type(object))
    else:
        print("Type not found")
    return 42
