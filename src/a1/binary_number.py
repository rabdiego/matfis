class BinaryNumber:
    def __init__(self, number_string: str = '0') -> None:
        if not self.validate_string(number_string):
            raise Exception('Existe algo de errado com sua string...')
        
        self.string = number_string


    def _xor(self, dig1: int, dig2: int) -> int:
        """
        Função auxiliar pra computar o xor
        """
        return int((dig1 and not dig2) or (not dig1 and dig2))


    def __str__(self) -> str:
        return self.string
    

    def validate_string(self, number_string: str) -> bool:
        """
        Validação (2 pontos)
        """
        if len(number_string) == 0:
            return False
        
        for char in number_string:
            if char not in ['0', '1']:
                return False
        
        return True


    def successor(self):
        """
        Sucessor (2 pontos)
        """
        string_reversed = self.string[::-1]
        new_string = ''
        carry = 1
        for char in string_reversed:
            digit = int(char)
            new_string += str(self._xor(digit, carry))  # XOR
            carry = int(digit and carry)  # AND
        string = new_string[::-1]
        return BinaryNumber(string)


    def inverse(self):
        """
        Inverso (1 ponto)
        """
        new_string = ''
        for char in self.string:
            digit = int(char)
            new_string += str(int(not digit))
        return BinaryNumber(new_string)
    

    def complet_2(self):
        """
        Complemento de 2 (2 pontos)
        """
        inverse = self.inverse()
        n_bits = len(self.string)
        
        # Criando um número representando o 1
        one_list = ['0' for _ in range(n_bits)]
        one_list[-1] = '1'

        one_str = ''
        for char in one_list:
            one_str += char
        
        one = BinaryNumber(one_str)

        return inverse + one


    def __add__(self, bn2):
        """
        Adição (2 pontos)
        """
        bn2_inv_str = bn2.string[::-1]
        bn1_inv_str = self.string[::-1]
        new_string = ''
        n_bits = len(bn1_inv_str)

        carry = 0

        for i in range(n_bits):
            bn1_digit = int(bn1_inv_str[i])
            bn2_digit = int(bn2_inv_str[i])

            new_digit = self._xor(self._xor(bn1_digit, bn2_digit), carry)
            carry = int(int(bn1_digit and bn2_digit) or int(self._xor(bn1_digit, bn2_digit) and carry))
            new_string += str(new_digit)
        
        new_string = new_string[::-1]
        return BinaryNumber(new_string)


    def __sub__(self, bn2):
        """
        Subtração (2 pontos)
        """
        bn2_minus = bn2.complet_2()
        return self + bn2_minus


    def and_bb(self, bn2):
        """
        AND bit a bit (0,75 ponto)
        """

        str_1 = self.string
        str_2 = bn2.string
        n_bits = len(str_1)
        new_str = ''

        for i in range(n_bits):
            dig_1 = int(str_1[i])
            dig_2 = int(str_2[i])

            new_str += str(int(dig_1 and dig_2))
        
        return BinaryNumber(new_str)


    def or_bb(self, bn2):
        """
        OR bit a bit (0,75 ponto)
        """

        str_1 = self.string
        str_2 = bn2.string
        n_bits = len(str_1)
        new_str = ''

        for i in range(n_bits):
            dig_1 = int(str_1[i])
            dig_2 = int(str_2[i])

            new_str += str(int(dig_1 or dig_2))
        
        return BinaryNumber(new_str)


    def xor_bb(self, bn2):
            """
            XOR bit a bit (0,75 ponto)
            """

            str_1 = self.string
            str_2 = bn2.string
            n_bits = len(str_1)
            new_str = ''

            for i in range(n_bits):
                dig_1 = int(str_1[i])
                dig_2 = int(str_2[i])

                new_str += str(self._xor(dig_1, dig_2))
            
            return BinaryNumber(new_str)

