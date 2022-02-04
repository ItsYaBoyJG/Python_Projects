NAME = input("Name: ")


# print(cap_name(NAME))

def solve(s):
    return " ".join([a.capitalize() for a in s.split(" ")])



print(solve(NAME))
