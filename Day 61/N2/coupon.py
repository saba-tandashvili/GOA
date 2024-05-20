def isValidCoupon(couponCode, totalAmount):
    if (couponCode == "SALE" or couponCode == "BIGSALE") and (totalAmount >= 50):
        return True
    elif couponCode == "LILSALE":
        return True
    else:
        return False