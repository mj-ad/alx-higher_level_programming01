#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hid
    for i in hid:
        if i[0] == '_':
            continue
        else:
            print(i);
