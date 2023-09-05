
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer,String,Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
class Base(DeclarativeBase):
    pass
class Planet(Base):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    diameter: Mapped[float] = mapped_column(Float)
    def __repr__(self) -> str:
        return f"Planet [ Id: {self.id}, Name: {self.name}, Diameter: {self.diameter} ]"