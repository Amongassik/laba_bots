from aiogram.fsm.state import State,StatesGroup
from typing import Optional,Dict
import math

class CaseState(StatesGroup):
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
        self.error: Optional[str] = None
        self.success:Optional[bool] = True
    
    def is_ready(self)->bool:
        return (self.f1 is not None) and (self.f2 is not None) and (self.f3 is not None)
    
    def check_success(self):
        return self.success
    
    def set_func(self,func_str:str,func_num:int):
        if func_num == 0:
            self.f1 = func_str
        elif func_num == 1:
            self.f2 = func_str
        elif func_num == 2:
            self.f3 = func_str
        else:
            self.success = False
            self.error = "Error Index Value"
    
    def set_x(self,x:float):
        if x is None:
            self.success = False
            self.error = "Ошибка:введите число"
            return
        if not isinstance(x,(int,float)):
            self.success = False
            self.error = f"Ошибка:занчение должно быть числом"
            return
        self.x = x
        self.success = True
        self.error = None
        self.result = None

    @classmethod
    def to_type_func(cls,func_str:str):
        return cls.FUNC_TYPES.get(func_str,'?')
    
    def to_formula(self):
        if not self.is_ready():
            self.success = False
            self.error = None
            return "Не все функции выбраны.Должно получится выражение: y = [F₁] ( [F₂] ( [F₃] ( x ) ) )"
        
        func_str =  f"({self.f1}({self.f2}({self.f3}(x))))"
        return f" Функция:y={func_str}"
    
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
            return 1/x
        if func_type == 'exp':
            try:
                return math.exp(x)
            except:
                self.success = False
                self.error = f"Ошибка: переполнение при вычислении e^{x}"
                return
        else:
            self.success = False
            self.error = f"Ошибка типа функции , вы не правильно ввели функцию"
            return
    
    def calculate(self):
        if not self.is_ready():
            self.success = False
            self.error = 'Не все функции заполенны'
            return
        func_types = [self.to_type_func(f) for f in [self.f3,self.f2,self.f1]]
        self.success = True
        if self.x is None:
            self.success = False
            self.error = "Не введено значение X"
            return
        result = self.x
        for f in func_types:
            result = self.apply_function(f,result)
            if not self.success:
                return
        self.message = f"Результат посчитан успешно:{result}"
        self.result = result
    
    def to_vba(self):
        """Возвращает код для VBA в виде строки (пока не надо реализовывать)"""
        pass

user_cases:Dict[int,CaseHandel] = {}

def get_user_case(user_id:int)->CaseHandel:
    if user_id not in user_cases:
        user_cases[user_id] = CaseHandel()
    return user_cases[user_id]    
