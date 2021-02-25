import forbiddenfruit as ff
from typing import Union

@ff.curses(list, "toString")
@ff.curses(tuple, "toString")
def ar_toString(self:Union[list, tuple]) -> str:
    return ','.join(str(i) for i in self)

@ff.curses(list, "join")
@ff.curses(tuple, "join")
def ar_join(self:Union[list, tuple], connector:str=",") -> str:
    return connector.join(str(i) for i in self)