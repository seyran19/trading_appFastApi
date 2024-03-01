from sqlalchemy import Integer, TIMESTAMP, String, Boolean
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Operation(Base):
    __tablename__ = 'operation'
    id = mapped_column(Integer, primary_key=True)
    quantity = mapped_column(String)
    figi = mapped_column(String)
    instrument_type = mapped_column(String, nullable=True)
    date = mapped_column(TIMESTAMP)
    type = mapped_column(String)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}