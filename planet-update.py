from db import session
from models import Planet
from sqlalchemy import select

stmt = select(Planet).where(Planet.id == 3)
record = session.scalars(stmt).one()
record.name = "Updated "+record.name 
session.commit()