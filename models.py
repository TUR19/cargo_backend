from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base


DB = declarative_base()


class TrackCode(DB):
    __tablename__ = 'trackCodes'

    id = Column(Integer, primary_key=True, index=True)
    trackCode = Column(Integer, index=True)
    dateRegistrationClient = Column(Boolean)
    receivedInStockInChina = Column(Boolean)
    receivedAtTheWarehouseInAlmaty = Column(Boolean)
    receivedByTheClient = Column(Boolean)




