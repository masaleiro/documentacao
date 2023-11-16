"""
módulo que implementa os métodos necessários para a conversão de unidades de distância.

:Date: nov, 2020
:Version: 1.0
:Authors: pcardoso
"""

_fator = {
    "mm": 0.001,
    "cm": 0.01,
    "dm": 0.1,
    "m": 1,
    "dam": 10,
    "hm": 100,
    "km": 1000,
    "mi": 1609.344,    # milhas
    "pe": 0.3048      # pés
    }
"""
fator de conversão de cada unidade para metros
"""


def converte_distancia(comprimento, de_unidade, para_unidade):
    """
    Conversor de distancia.
    Recebe o valor da distancia e correspondente unidade e devolve a distancia na unidade pretendida.

    :param comprimento: distancia original
    :type comprimento: int ou float
    :param de_unidade: unidade da distancia original (valores admissíveis: fator.keys())
    :type de_unidade: string
    :param para_unidade: unidade da distancia pretendida (valores admissíveis: fator.keys())
    :type para_unidade: string
    :return: comprimento na unidade pretendida
    :rtype: float
    :raises TypeError: se os tipos não forem os corretos

    :Exemplo:

    >>> converte_distancia(10, "m", "km")
    0.01
    """
    assert isinstance(comprimento, (int, float)), "comprimento deve ser int ou float"
    assert isinstance(de_unidade, str), f"unidade deve ser elemento de {list(_fator.keys())}"
    assert isinstance(para_unidade, str), f"unidade deve ser elemento de {list(_fator.keys())}"

    return comprimento * _fator[de_unidade] / _fator[para_unidade]


def menu_distancia():
    """
    Função para gerir o menu dos conversores de distância.
    Apresenta um menu e de acordo com as opção escolhida pelo utilizador chamas as funções de conversão
    """

    while True:
        print(f"""
             -----------------------------  converte distâncias ------------------------------
             Unidades possíveis: {list(_fator.keys())}
             exemplo:
               de = 10 m    # colocar espaço a seguir ao número
               para = km

               km = 10000 m
             (S)air
             """)

        try:
            de_str = input("de?").lower()
            if de_str == "s":
                break
            comprimento, de_unidade = de_str.split()
            comprimento = float(comprimento)
            assert de_unidade in _fator.keys(), "Unidade inválida"

            para_unidade = input("para?").lower()
            assert para_unidade in _fator.keys(), "Unidade inválida"

            print(f"{de_str} = {converte_distancia(comprimento, de_unidade, para_unidade)} {para_unidade}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    converte_distancia("1", "mm", "km")
    print("over & out!")
