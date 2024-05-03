def fake_bin(x):
    back = ""
    for num in x:
        if int(num) < 5:
            back = back + "0"
        else:
            back = back + "1"
    return back