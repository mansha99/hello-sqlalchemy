from db import session
from models import Planet
planet1=Planet(name="Mercury",diameter=4879)
planet2=Planet(name="Venus",diameter=12104)
planet3=Planet(name="Earth",diameter=12756)
planet4=Planet(name="Mars",diameter=6792)
session.add_all([planet1,planet2,planet3,planet4])
session.commit()