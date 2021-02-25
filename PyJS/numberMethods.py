import forbiddenfruit as ff

@ff.curses(float, "toString")
@ff.curses(int, "toString")
@ff.curses(complex, "toString")
def num_toString(self) -> str:
    return str(self)

@ff.curses(float, "toExponential")
@ff.curses(int, "toExponential")
@ff.curses(complex, "toExponential")
def num_toExponential(self, N=1) -> str:
    return format(self, f'0.{N}e')

@ff.curses(float, "toFixed")
@ff.curses(int, "toFixed")
@ff.curses(complex, "toFixed")
def num_toFixed(self, N=1) -> str:
    return format(self, f"0.{N}f")

@ff.curses(float, "valueOf")
@ff.curses(int, "valueOf")
@ff.curses(complex, "valueOf")
def num_valueOf(self):
    return self