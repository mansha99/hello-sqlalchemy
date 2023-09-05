from db import session
from models import Planet
from sqlalchemy import select

results = session.query(Planet).where(Planet.id  > 1).order_by(Planet.diameter).limit(2).offset(2)

for record in results:
    print(record)

