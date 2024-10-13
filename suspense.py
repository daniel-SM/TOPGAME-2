# Importando para dar pausas
from time import sleep


# Funcao para reproduzir um tempo de espera apos uma acao
def make_suspense(suspense_time: int) -> None:
    for _ in range(3):
        print(".")
        sleep(suspense_time)
