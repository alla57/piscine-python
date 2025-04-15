def NULL_not_found(object: any) -> int:
    if object == "Brian":
        print("Type not Found")
    elif object is None:
        print("Nothing:", object, type(object))
    elif isinstance(object, float):
        print("Cheese:", object, type(object))
    elif type(object) is int:
        print("Zero:", object, type(object))
    elif isinstance(object, str):
        print("Empty:", type(object))
    elif isinstance(object, bool):
        print("Fake:", object, type(object))
    return 1