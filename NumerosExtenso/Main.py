from Extenso import Extenso


class Main:
    @staticmethod
    def traduzir(numero: str) -> None:
        print(Extenso.por_extenso(numero))


if __name__ == '__main__':
    valor: str = input("Informe o número: ")
    Main.traduzir(numero=valor)
