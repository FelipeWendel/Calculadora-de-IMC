def calcula_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura.

    Args:
        peso (float): Peso do usuário em kg.
        altura (float): Altura do usuário em metros.

    Returns:
        float: IMC do usuário.
    """
    imc = peso / (altura ** 2)
    return imc

def classifica_imc(imc):
    """
    Classifica o IMC de acordo com a tabela da OMS.

    Args:
        imc (float): IMC do usuário.

    Returns:
        str: Classificação do IMC.
    """
    if imc < 18.5:
        return "Magreza"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcula_imc(peso, altura)
    classificacao = classifica_imc(imc)

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()