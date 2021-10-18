def run(num, modu):
    mod = num % modu
    print("The modulus is " + str(mod))


if __name__ == "__main__":
    num = int(input("Take this number by modulo: "))
    modulus = int(input("Modulus number: "))
    run(num, modulus)
