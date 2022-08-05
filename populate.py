import random

from sqlmodel import Session
from models.perfume_model import Perfume, PerfumeColor,PerfumeProperties,PerfumeClass,PerfumeType
from main import engine

perfume_colors = list(PerfumeColor)
perfume_classes = list(PerfumeClass)
perfume_types = list(PerfumeType)


def create_perfume_properties():
    
    color = random.choice(perfume_colors)
    perfume_for = random.choice(perfume_classes)
    perfume_properties = PerfumeProperties(perfume_class=perfume_for,color=color)
    
    return perfume_properties

def create_perfume(perfume_properties):
    perfume_type = random.choice(perfume_types)
    price = random.randint(1000,2000)
    perfume = Perfume(price=price,perfume_properties_id=perfume_properties,perfume_type=perfume_type)
    
    return perfume

def create_perfume_db():
    prefume_prop = create_perfume_properties()
    print(prefume_prop)

    with Session(engine) as session:
        session.add(prefume_prop)
        session.commit()
        perfume = create_perfume(prefume_prop.id)
        session.add(perfume)
        session.commit()

create_perfume_db()
