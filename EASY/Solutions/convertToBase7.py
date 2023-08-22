def convertToBase7(num: int) -> str:
    if num == 0:
        return "0"
    negative = False
    if num < 0:
        num *= -1
        negative = True
    baseSeven = ""
    while num > 0:
        remainder = num % 7
        baseSeven += str(remainder)
        num //= 7
    baseSeven = baseSeven[::-1]
    if negative: baseSeven = "-"+baseSeven
    return baseSeven
