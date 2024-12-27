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


    def __add__(self, v2):
        v3 = Vector([0 for _ in range(self.N)])  # Vetor "placeholder"

        for idx in range(self.N):
            v3[idx] = self[idx] + v2[idx]
        
        return v3


    def __sub__(self, v2):
        v3 = Vector([0 for _ in range(self.N)])  # Vetor "placeholder"

        for idx in range(self.N):
            v3[idx] = self[idx] - v2[idx]
        
        return v3
    

    def __neg__(self):
        v2 = Vector([0 for _ in range(self.N)])  # Vetor "placeholder"

        for idx, element in enumerate(self.data):
            v2[idx] = -element
        
        return v2


    def _scalar_multiplication(self, scalar: float):
        v2 = Vector([0 for _ in range(self.N)])  # Vetor "placeholder"

        for idx, element in enumerate(self.data):
            v2[idx] = scalar * element
        
        return v2
    

    def _dot_product(self, v2) -> float:
        s = 0

        for idx in range(self.N):
            s += self[idx]*v2[idx]
        
        return s

