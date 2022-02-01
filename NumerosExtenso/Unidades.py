class Unidades:
    @staticmethod
    def unidades(numero: str) -> str:
        valor: str
        match numero:
            case "1":
                valor = "um"
                return valor
            case "2":
                valor = "dois"
                return valor
            case "3":
                valor = "três"
                return valor
            case "4":
                valor = "quatro"
                return valor
            case "5":
                valor = "cinco"
                return valor
            case "6":
                valor = "seis"
                return valor
            case "7":
                valor = "sete"
                return valor
            case "8":
                valor = "oito"
                return valor
            case "9":
                valor = "nove"
                return valor
            case "10":
                valor = "dez"
                return valor


if __name__ == '__main__':
    numero: str = input("Digite o número: ")
    Unidades.unidades(numero)