from aiogram.fsm.state import State,StatesGroup
from typing import Optional,Dict,Any
import math

class CaseState(StatesGroup):
    for_f1 = State()
    for_f2 = State()
    for_f3 = State()
    for_x = State()

class CaseHandel:
    FUNC_TYPES={
        "√x":"sqrt",
        "1/x":"inv",
        "e^x":"exp"
    }

    def __init__(self):
        self.reset()
    
    def reset(self):
        self.f1: Optional[str] = None
        self.f2: Optional[str] = None
        self.f3: Optional[str] = None
        self.x: Optional[float] = None
        self.result: Optional[float] = None
        self.message:Optional[str] = None
        self.error: Optional[str] = True
        self.success:Optional[bool] = None
    
    def is_ready(self)->bool:
        return (self.f1 is not None) and (self.f2 is not None) and (self.f3 is not None)
    
    def set_func(self,func_str:str,func_num:int):
        if func_num == 1:
            self.f1 = func_str
        elif func_num == 2:
            self.f2 = func_str
        elif func_num == 3:
            self.f3 = func_str
        else:
            self.success = False
            self.error = "Error Index Value"

    @classmethod
    def to_type_func(cls,func_str:str):
        return cls.FUNC_TYPES.get(func_str,'?')
    
    def apply_function(self,func_type:str,x:float):
        if func_type == 'sqrt':
            if x<0:
                self.success = False
                self.error = f"Ошибка области определения в {x} при вычислении √x"
                return
            return math.sqrt(x)
        if func_type == 'inv':
            if x==0:
                self.success = False
                self.error = f"Ошибка области определения в {x} при вычислении 1/x"
                return
            else:
                return 1/x
        if func_type == 'exp':
            try:
                return math.exp(x)
            except:
                self.success = False
                self.error = f"Ошибка: переполнение при вычислении e^{x}"
        else:
            self.success = False
            self.error = f"Ошибка типа функции , вы не правильно ввели функцию"
            return
    
    def calculate(self,x:float):
        func_types = [self.to_type_func(f) for f in [self.f3,self.f2,self.f1]]
        result = x
        for f in func_types:
            result = self.apply_function(f,result)
            if not self.success:
                return
        self.message = f"Результат посчитан успешно"
    
    @classmethod
    def to_vba(cls):
        """Возвращает код для VBA в виде строки (пока не надо реализовывать)"""
        pass


        
        
    

            
    

    
