
class Numbers:
    """
    :argument number -> int, number being tested
    """
    def __int__(self, number: int):
        self.number = number

    def is_even(self) -> bool:
        return self.number > 0 and self.number % 2 == 0

    def is_odd(self) -> bool:
        return self.number > 0 and self.number % 2 == 1



