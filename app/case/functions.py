import math
from typing import Tuple,Optional
from enum import Enum

class FuncType(Enum):
    SQRT = 'sqrt'
    INV = 'inv'
    EXP = 'exp'

def apply_function(func_type:str,x:float)->Tuple[bool,float,str]:
    """
    Применение функции к значению
    Args:
        func_type:тип функции
        x:входное значение
    Returns:
        (success,value,message)
    """
    if func_type == 'sqrt':
        if x<0:
            return False,0,f"Ошибка значение {x} не входит в область определения функции "
        return True, math.sqrt(x),""
    elif func_type == 'inv':
        if x==0:
            return False,0,f"Ошибка занчения {x}"
        return True,1/x,""
    elif func_type == 'exp':
        try:
            return True,math.exp(x),""
        except OverflowError:
            return False,0,f"Ошибка:переполнение кеша при вычислении e^{x}"
    else:
        return False,0,f"Неизвестная функция {func_type}"

def get_func_name(func_type: str) -> str:
    """Возвращает читаемое название функции"""
    names = {
        'sqrt': '√x (квадратный корень)',
        'inv': '1/x (обратное число)',
        'exp': 'e^x (экспонента)'
    }
    return names.get(func_type, func_type)

def get_func_symbol(func_type: str) -> str:
    """Возвращает символ функции для отображения"""
    symbols = {
        'sqrt': '√',
        'inv': '1/',
        'exp': 'e^'
    }
    return symbols.get(func_type, '?')
