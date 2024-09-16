from ..models.venue import Venue
from sqlmodel import Session
from ..db.db import create_db_and_tables, engine

create_db_and_tables()

def insert_venues(engine):
    venues_data = [
        {"name": "Impact Arena", "capacity": 20000},
        {"name": "Rajamangala National Stadium", "capacity": 50000},
        {"name": "GMM Live House", "capacity": 3000},
        {"name": "Thunder Dome", "capacity": 10000},
        {"name": "Central World Arena", "capacity": 7000},
        {"name": "Queen Sirikit National Convention Center", "capacity": 15000},
        {"name": "BITEC Bangna", "capacity": 20000},
        {"name": "MCC Hall", "capacity": 5000},
        {"name": "Siam Paragon Hall", "capacity": 4000},
        {"name": "MBK Center", "capacity": 3000}
    ]

    with Session(engine) as session:
        for venue_data in venues_data:
            venue = Venue(**venue_data)
            session.add(venue)
        session.commit()