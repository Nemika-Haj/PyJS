import forbiddenfruit as ff
from typing import Union

def ar_toString(self:Union[list, tuple]) -> str:
    return ','.join(str(i) for i in self)

def ar_join(self:Union[list, tuple], connector:str=",") -> str:
    return connector.join(str(i) for i in self)

ff.curse(list, "toString", ar_toString)
ff.curse(tuple, "toString", ar_toString)
ff.curse(list, "join", ar_join)
ff.curse(tuple, "join", ar_join)