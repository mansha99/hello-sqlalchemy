from db import session
from models import Planet

record1 = session.get(Planet, 1)
if record1 is None:
    print('----- No Planet exist with id 1')
else:
    print('----- Planet exist with id 1')
    session.delete(record1)
    print('----- Planet DELETED id 101')
    

record99 = session.get(Planet, 99)
if record99 is None:
    print('----- No Planet exist with id 99')
else:
    print('----- Planet exist with id 99')
    session.delete(record99)
    print('----- Planet DELETED id 99')
    
session.commit()
