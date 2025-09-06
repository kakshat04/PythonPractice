def base_feature(func):  #pylint: disable=invalid-name
    def wrapper(*args, **kwargs):
        print("This is base feature")
        func(*args, **kwargs)
    return wrapper



@base_feature
def new_feature(feature):
    print(f"New feature is {feature}")

new_feature("gps")