def calcular_media(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")

    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def calcular_resultado(notas):
    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    return {
        "media": media,
        "situacao": situacao
    }        float(input("Digite a primeira nota: ")),
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
