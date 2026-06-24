string = "task del complete nothig // 2" # for testing only

def parse(string): # prototype
    parts = string.strip().split(" ", 2) # split query into first word, second word and rest of words
    partsAmt = len(parts)

    family = (parts[0] if partsAmt > 0 else "").lower() # first word
    action = (parts [1] if partsAmt > 1 else "").lower() # second word

    args = parts[2] if partsAmt > 2 else "" # if no arg is provided, "" is given as arg

    if args:
        args = [arg.strip() for arg in args.split("//")] # seperates args by "//" and strips them, returning list of args
    else:
        args = []

    return {
        "family": family,
        "action": action,
        "args": args,
    }

if __name__ == "__main__":
    print(parse(string)) # test case