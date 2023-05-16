# klasa lub funkcje do działań + zarządzanie, dict zamiast ifelse

class Calculator:
    def __init__(self, operation, a, b):
        self.operation = operation
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_operation(self):
        return self.operation

    def get_sign(self):
        d = self.operation_type()[self.operation]
        return d["sign"]

    def get_math(self):
        d = self.operation_type()[self.operation]
        return d["math"]

    def check_if_zero(self): # może to nie najładniejsze rozwiązanie, ale lambda w słowniku nie przechodziła :(
        return self.a / self.b if self.b != 0 else "dzielenie przez 0 to zło"

    def operation_type(self):
        division = self.check_if_zero()
        return {
            "add": {
                "sign": "+",
                "math": self.a + self.b,
            },
            "sub": {
                "sign": "-",
                "math": self.a - self.b,
            },
            "mul": {
                "sign": "*",
                "math": self.a * self.b,
            },
            "div": {
                "sign": "/",
                "math": division,
            },
        }
