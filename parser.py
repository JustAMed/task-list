string = "add address thingy // address is zero"

def parse(string):
    parts = string.strip().split(" ", 1)
    action = parts[0]
    args = parts[1] if len(parts) > 1 else ""
    args = args.split(" /// ")
    return (action, args)