def display_info(data, /, *, reverse=False, uppercase=False):
    result = data

    if reverse:
        result = result[::-1]

    if uppercase:
        result = result.upper()

    return result

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC