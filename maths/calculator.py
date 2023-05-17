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
        return self.div() if self.b != 0 else "dzielenie przez 0 to zło"

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def operation_type(self):
        return {
            "add": {
                "sign": "+",
                "math": self.add(),
            },
            "sub": {
                "sign": "-",
                "math": self.sub(),
            },
            "mul": {
                "sign": "*",
                "math": self.mul(),
            },
            "div": {
                "sign": "/",
                "math": self.check_if_zero(),
            },
        }
# warning: in the working copy of '.idea/inspectionProfiles/profiles_settings.xml', LF will be replaced by CRLF the next time Git touches it
# maths/__pycache__/calculator.cpython-38.pyc