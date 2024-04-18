def baseToDec(number : str, base : int):
    number, result = number.split(","), 0
    for value in range(len(number)-1): result += int(number[len(number)-value]) * (base**value)
    return result
    
def decToBase(number : int, base : int):
    result = ""
    while number >= base: number ,result = number // base,f'{number % base},' + result
    return result[:-1]
    
def main():
    iN, iB, oB = input("Input number:\n"), int(input("Input base:\n")), int(input("Output base:\n"))
    print(decToBase(baseToDec(iN, iB), oN)
