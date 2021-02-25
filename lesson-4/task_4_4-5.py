from utils import currency_rates

# print(f"Вон Республики Корея: {currency_rates('KRW')}")
# print(f"Турецкая лира: {currency_rates('try')}")
# print(f"Казахстанский тенге: {currency_rates('kzt')}")
# print(f"Несуществующая валюта: {currency_rates('ывыа')}")


def main(argv):
    program, *args = argv
    for i in args:
        result = currency_rates(i)
        print(result)

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
