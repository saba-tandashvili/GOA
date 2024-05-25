function isTeenager(age, hasPermission) {
    if ((age < 18 && !hasPermission) || (age === 18 && hasPermission)) {
        return true;
    } else {
        return false;
    }
}