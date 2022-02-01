class Centenas:
    @staticmethod
    def centenas(numero: str) -> str:

        match numero[0]:
            case "1":
                if numero[1] == "0" and numero[2] == "0":
                    return "cem"
                else:
                    return "cento"
            case "2":
                return "duzentos"
            case "3":
                return "trezentos"
            case "4":
                return "quatrocentos"
            case "5":
                return "quinhetos"
            case "6":
                return "seicentos"
            case "7":
                return "setecentos"
            case "8":
                return "oitocentos"
            case "9":
                return "novecentos"
