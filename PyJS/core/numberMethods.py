import forbiddenfruit as ff

def num_toString(self) -> str:
    return str(self)

def num_toExponential(self, N=1) -> str:
    return format(self, f'0.{N}e')

def num_toFixed(self, N=1) -> str:
    return format(self, f"0.{N}f")

def num_valueOf(self):
    return self

ff.curse(float, "toString", num_toString)
ff.curse(int, "toString", num_toString)
ff.curse(int, "toExponential", num_toExponential)
ff.curse(float, "toExponential", num_toExponential)
ff.curse(int, "toFixed", num_toFixed)
ff.curse(float, "toFixed", num_toFixed)
ff.curse(int, "valueOf", num_valueOf)
ff.curse(float, "valueOf", num_valueOf)