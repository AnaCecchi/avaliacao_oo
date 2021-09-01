class Soma:


    @staticmethod
    def soma_numeros(array):
        result = 0
        for numero in array:
            result = result + numero
        return result
array = [2,4,5]

resultado = Soma.soma_numeros(array)
print(resultado)
