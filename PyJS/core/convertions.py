import forbiddenfruit as ff 

__all__ = (
    "parseInt",
    "parseFloat",
    "Number"
)

def parseInt(self) -> int:
    try:
        return int(self)
    except: return None

def parseFloat(self) -> float:
    try:
        return float(self)
    except: return None

class Number:
    def __init__(self, nmr=None):
        try:
            self.num = float(nmr)
        except:
            self.num = None
        
    def __float__(self):
        return self.num
    
    def __int__(self):
        return self.num
    
    def __str__(self):
        return str(self.num)

    def MAX_VALUE() -> complex:
        return 1.7976931348623157e+308

    def MIN_VALUE() -> complex:
        return 5e-324

    def MAX_SAFE_INTEGER() -> int:
        return 9007199254740991
    
    def MIN_SAFE_INTEGER() -> int:
        return -9007199254740991