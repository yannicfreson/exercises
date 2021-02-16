# Write your code here
def slug(name):
    parts = name.split(" ")
    first = parts[0]
    last = parts[1:]
    return "-".join(string.lower() for string in last + [first])