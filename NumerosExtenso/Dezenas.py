class Dezenas:
    @staticmethod
    def dezenas(numero: str) -> str:
        match numero:
            case "10":
                return "dez"
            case "11":
                return "onze"
            case "12":
                return "doze"
            case "13":
                return "treze"
            case "14":
                return "catorze"
            case "15":
                return "quinze"
            case "16":
                return "dezeseis"
            case "17":
                return "dezesete"
            case "18":
                return "dezoito"
            case "19":
                return "dezenove"
            case "20":
                return "vinte"
            case None:
                print('')
