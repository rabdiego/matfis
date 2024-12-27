class Vector:
    def __init__(self, data: list) -> None:
        self.data = data.copy()
        self.N = len(data)

    
    # Os próximos 3 métodos são feitos para facilitar a nossa vida na hora de escrever as outras funções :)
    def __getitem__(self, idx):
        return self.data[idx]
    

    def __setitem__(self, idx, value):
        self.data[idx] = value

    
    def __str__(self):
        return str(self.data)


    def get_mag(self) -> float:
        """
        Método auxiliar para pegar ||v||
        """
        s = 0
        for element in self.data:
            s += element
        return s


    def norm(self):
        """
        Método auxiliar para normalizar um vetor
        """
        return self/self.get_mag()



    def __add__(self, v2):
        """
        Adição de 2 vetores
        """
        v3 = Vector([0 for _ in range(self.N)])  # Vetor "placeholder"

        for idx in range(self.N):
            v3[idx] = self[idx] + v2[idx]
        
        return v3


    def __sub__(self, v2):
        """
        Subtração de 2 vetores
        """
        v3 = Vector([0 for _ in range(self.N)])  # Vetor "placeholder"

        for idx in range(self.N):
            v3[idx] = self[idx] - v2[idx]
        
        return v3
    

    def __neg__(self):
        """
        Negação de um vetor
        """
        v2 = Vector([0 for _ in range(self.N)])  # Vetor "placeholder"

        for idx, element in enumerate(self.data):
            v2[idx] = -element
        
        return v2


    def __mul__(self, v2):
        """
        Multiplicação de um vetor por:
        (1) um escalar, ou
        (2) produto escalar,

        dependendo do tipo do que é passado.

        Não é implementado nesse operator overload o produto vetorial, pois
        este possui propriedades anticomutativas que "bugariam" usando o __mul__ do
        Python
        """
        if type(v2) == int or type(v2) == float:
            return self._scalar_multiplication(v2)
        
        return self._dot_product(v2)
    

    def __truediv__(self, scalar: float):
        """
        Método auxiliar para dividir um vetor por um escalar
        """

        v2 = Vector([0 for _ in range(self.N)])  # Vetor "placeholder"

        for idx, element in enumerate(self.data):
            v2[idx] = element / scalar
        
        return v2


    def _scalar_multiplication(self, scalar: float):
        """
        Multiplicação por escalar
        """
        v2 = Vector([0 for _ in range(self.N)])  # Vetor "placeholder"

        for idx, element in enumerate(self.data):
            v2[idx] = scalar * element
        
        return v2
    

    def _dot_product(self, v2) -> float:
        """
        Produto escalar
        """
        s = 0

        for idx in range(self.N):
            s += self[idx]*v2[idx]
        
        return s
    

    def cross(self, v2):
        """
        Produto vetorial

        Utilizei a definição pela fórmula da determinante
        """

        v3 = Vector([0 for _ in range(3)])  # Placeholder

        v3[0] = self[1]*v2[2] - self[2]*v2[1]
        v3[1] = -(self[0]*v2[2] - self[2]*v2[0])
        v3[2] = self[0]*v2[1] - self[1]*v2[0]

        return v3
    

    def project(self, v2):
        """
        Projeção de um vetor em outro

        No caso, usar v1.project(v2) retornará
        o vetor v1 projetado em v2.
        """
        aux1 = self * v2
        aux2 = v2 * v2
        return v2 * (aux1/aux2)
    

    def reflect(self, v2):
        """
        Reflexão

        No caso, usar v1.reflect(v2) retornará
        o vetor v3 que é a reflexão de v1 sobre a
        "reta" v2
        """

        v2_norm = v2.norm()
        return self - v2_norm*(2*(self * v2_norm))


    def slide(self, v2):
        """
        Deslizamento sobre uma parede, assumindo v2 como vetor unitário
        """

        return self - v2*(self*v2)

