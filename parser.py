string = "add address thingy // address is zero" # for testing only

def parse(string): # prototype
    parts = string.strip().split(" ", 1) # split query into first word and rest of words
    action = parts[0]
    args = parts[1] if len(parts) > 1 else "" # if no arg is provided, "" is given as arg
    args = args.split(" /// ") # split the args further
    return (action, args)

if __name__ == "__main__":
    print(parse(string)) # test case