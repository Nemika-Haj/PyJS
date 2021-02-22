import forbiddenfruit as ff

@property
def str_length(self) -> int:
    return len(self)

def str_search(self, other) -> int:
    return self.find(other)

def str_indexOf(self, other, startPos:int=0) -> int:
    return self[startPos:].find(other)

def str_lastIndexOf(self, other, startPos:int=0) -> int:
    return self[startPos:].rfind(other)

def str_slice(self, start=None, end=None) -> str:
    if not start:
        return self
    if not end:
        return self[start]
    return self[start:end]

def str_substring(self, start=None, end=None) -> str:
    if not start:
        return self
    if not end:
        if start < 0: raise ValueError("str.substring() cannot take negative indexes.")
        return self[start]
    if start < 0 or end < 0: raise ValueError("str.substring() cannot take negative indexes.")
    return self[start:end]

def str_toUpperCase(self) -> str:
    return self.upper()

def str_toLowerCase(self) -> str:
    return self.lower()

def str_concat(self, *other) -> str:
    return self + ''.join(other)

def str_trim(self) -> str:
    return self.strip()

def str_padStart(self, maxLength:int, fillString) -> str:
    return str(fillString)*(maxLength-1) + self

def str_padEnd(self, maxLength:int, fillString) -> str:
    return self + str(fillString)*(maxLength-1)

def str_charCodeAt(self, index=0) -> int:
    return ord(self[index])

ff.curse(str, "length", str_length)
ff.curse(str, "indexOf", str_indexOf)
ff.curse(str, "lastIndexOf", str_lastIndexOf)
ff.curse(str, "search", str_search)
ff.curse(str, "slice", str_slice)
ff.curse(str, "substring", str_substring)
ff.curse(str, "toUpperCase", str_toUpperCase)
ff.curse(str, "toLowerCase", str_toLowerCase)
ff.curse(str, "concat", str_concat)
ff.curse(str, "trim", str_trim)
ff.curse(str, "padStart", str_padStart)
ff.curse(str, "padEnd", str_padEnd)
ff.curse(str, "charCodeAt", str_charCodeAt)