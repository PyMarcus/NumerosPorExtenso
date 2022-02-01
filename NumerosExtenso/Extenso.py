from Unidades import Unidades
from Dezenas import Dezenas
from Centenas import Centenas

def intervalo(numero: str):
    valor = ""
    match numero[0]:
        case "2":
            valor = "vinte"
            return valor
        case "3":
            valor = "trinta"
            return valor
        case "4":
            valor = "quarenta"
            return valor
        case "5":
            valor = "cinquenta"
            return valor
        case "6":
            valor = "sessenta"
            return valor
        case "7":
            valor = "setenta"
            return valor
        case "8":
            valor = "oitenta"
            return valor
        case "9":
            valor = "noventa"
            return valor

class Extenso:
    @staticmethod
    def por_extenso(numero: str) -> str:
        if len(numero) < 2 or numero == '10':
            return str(Unidades.unidades(numero))
        elif len(numero) == 2 and numero[0] == "1":
            return str(Dezenas.dezenas(numero))
        elif len(numero) == 2 and numero[0] != "1":
            if Unidades.unidades(numero[1]):
                return intervalo(numero[0]) + " e " + Unidades.unidades(numero[1])
            else:
                return intervalo(numero[0])
        else:
            if numero[1] != '1':
                if intervalo(numero[1]) != None and Unidades.unidades(numero[2]) != None:
                    return  Centenas.centenas(numero) + " e " + intervalo(numero[1]) + " e " + Unidades.unidades(numero[2])
                elif intervalo(numero[1]) == None and Unidades.unidades(numero[2]) != None:
                    return Centenas.centenas(numero) + " e " + str(Unidades.unidades(numero[2]))
                elif intervalo(numero[1]) == None and Unidades.unidades(numero[2]) == None:
                    return Centenas.centenas(numero)
                elif intervalo(numero[1]) != None and Unidades.unidades(numero[2]) == None:
                    return Centenas.centenas(numero) + " e " + intervalo(numero[1])
            else:
                if Dezenas.dezenas(numero[1:]):
                    return Centenas.centenas(numero) + " e " + Dezenas.dezenas(numero[1:])
                else:
                    return Centenas.centenas(numero)

if __name__ == '__main__':
    while True:
        try:
            numero: str = input(">>> ")
        except KeyboardInterrupt or EOFError:
            pass
        finally:
            print(Extenso.por_extenso(numero))
