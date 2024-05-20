def isTeenager(age, hasPermission):
    if (age >= 13 and age <= 19) and (not hasPermission):
        return False
    elif (age == 18 and hasPermission):
        return True
    else:
        return False