'''Bank Notes'''
def main():
    '''Function'''
    bank = int(input())
    print(bank // 1000)
    bank = bank % 1000
    print(bank // 500)
    bank = bank % 500
    print(bank // 100)
    bank = bank % 100
    print(bank // 50)
    bank = bank % 50
    print(bank // 20)
    bank = bank % 20
    print(bank // 10)

main()
