import forbiddenfruit as ff

@ff.curses(str, "length")
@property
def str_length(self) -> int:
    return len(self)

@ff.curses(str, "search")
def str_search(self, other) -> int:
    return self.find(other)

@ff.curses(str, "indexOf")
def str_indexOf(self, other, startPos:int=0) -> int:
    return self[startPos:].find(other)

@ff.curses(str, "lastIndexOf")
def str_lastIndexOf(self, other, startPos:int=0) -> int:
    return self[startPos:].rfind(other)

@ff.curses(str, "slice")
def str_slice(self, start=None, end=None) -> str:
    if not start:
        return self
    if not end:
        return self[start]
    return self[start:end]

@ff.curses(str, "substring")
def str_substring(self, start=None, end=None) -> str:
    if not start:
        return self
    if not end:
        if start < 0: raise ValueError("str.substring() cannot take negative indexes.")
        return self[start]
    if start < 0 or end < 0: raise ValueError("str.substring() cannot take negative indexes.")
    return self[start:end]

@ff.curses(str, "toUpperCase")
def str_toUpperCase(self) -> str:
    return self.upper()

@ff.curses(str, "toLowerCase")
def str_toLowerCase(self) -> str:
    return self.lower()

@ff.curses(str, "concat")
def str_concat(self, *other) -> str:
    return self + ''.join(other)

@ff.curses(str, "trim")
def str_trim(self) -> str:
    return self.strip()

@ff.curses(str, "padStart")
def str_padStart(self, maxLength:int, fillString) -> str:
    return str(fillString)*(maxLength-1) + self

@ff.curses(str, "padEnd")
def str_padEnd(self, maxLength:int, fillString) -> str:
    return self + str(fillString)*(maxLength-1)

@ff.curses(str, "charCodeAt")
def str_charCodeAt(self, index=0) -> int:
    return ord(self[index])