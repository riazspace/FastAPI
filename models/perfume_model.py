from sqlmodel import SQLModel, Field
from enum import Enum
from typing import Optional

class PerfumeClass(str,Enum):
    PREMIUM = 'PREM'
    EXCLUSIVE = "EXC"
    AVERAGE = "AVG"

class PerfumeColor(str,Enum):
    GOLD = 'Golden'
    TRANSPARENT = 'Transparent'
    SILVER = 'Silver' 

class PerfumeProperties(SQLModel,table = True):
    id: Optional[int] = Field(primary_key = True)
    perfume_class: Optional[PerfumeClass] = None
    color: Optional[PerfumeColor] = None


class PerfumeType(str,Enum):
    FOR_GENTS = 'Gents'
    FOR_LADIES = 'Ladies'
    FOR_ALL = 'All'



class Perfume(SQLModel,table=True):
    id: Optional[int] = Field(primary_key=True)
    price: float = 1
    available :  bool = True
    perfume_type : PerfumeType = PerfumeType.FOR_ALL

    perfume_properties_id : Optional[int] = Field(default=None,foreign_key='perfumeproperties.id')


