class Celula:

    def __init__(self, proxima, celula):
        self.__proxima = proxima
        self.__aluno = celula

    @property
    def proximo(self):
        return self.__proxima

    @proximo.setter
    def proximo(self, proxima):
        self.__proxima = proxima

    @property
    def aluno(self):
        return self.__aluno

    def __str__(self):
        return self.__aluno


    def __str__(self):
        return self.__aluno