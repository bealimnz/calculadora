class Calculator:
    """
    Uma classe simples para realizar operações aritméticas básicas.
    """

    def add(self, a: float, b: float) -> float:
        """Soma dois números (a + b)."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtrai o segundo número do primeiro (a - b)."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplica dois números (a * b)."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divide o primeiro número pelo segundo (a / b).
        Levanta um ValueError se o divisor (b) for zero.
        """
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """
        Calcula a potência de uma base elevada a um expoente (base ** exponent).
        """
        return base ** exponent

    def square_root(self, number: float) -> float:
        """
        Calcula a raiz quadrada de um número.
        Levanta um ValueError se o número for negativo.
        """
        if number < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
        return number ** 0.5