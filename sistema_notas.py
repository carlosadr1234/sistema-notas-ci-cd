def calcular_media(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")

    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("As notas devem estar entre 0 e 10.")

    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def maior_nota(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")

    return max(notas)


def menor_nota(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")

    return min(notas)


def resumo_aluno(nome, notas):
    media = calcular_media(notas)

    return {
        "nome": nome,
        "media": round(media, 2),
        "situacao": verificar_situacao(media),
        "maior_nota": maior_nota(notas),
        "menor_nota": menor_nota(notas),
    }


if __name__ == "__main__":
    nome = input("Nome do aluno: ")

    notas = [
        float(input("Digite a primeira nota: ")),
        float(input("Digite a segunda nota: ")),
        float(input("Digite a terceira nota: "))
    ]

    resultado = resumo_aluno(nome, notas)

    print("\n--- Resultado ---")
    print(f"Aluno: {resultado['nome']}")
    print(f"Média: {resultado['media']}")
    print(f"Situação: {resultado['situacao']}")
    print(f"Maior nota: {resultado['maior_nota']}")
    print(f"Menor nota: {resultado['menor_nota']}")
