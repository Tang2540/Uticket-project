from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional, Union

app = FastAPI()

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    userid: int
    username: str
    email: EmailStr



class Events(BaseModel):
    eventid: int
    eventname: str
    venue: str
    eventdate: str
    available_tickets: int

class Payment(BaseModel):
    paymentid: int
    status: str
    PaymentMethod: str

class Seats(BaseModel):
    seatid: int
    seatposition: str
    zone: str

class Ticket(BaseModel):
    name: str
    description: Optional[str] = ''
    price: float
    tax: Optional[float] = 0
    tags: List[str] = []
    pic: str

class Venue(BaseModel):
    id: int
    name: str
    capacity: int
    
class OrganizerAlter(BaseModel):
    name:str
    email:str
    
class Organizer(OrganizerAlter):
    id: int

class Booking(BaseModel):
    bookingid: int
    userid: int
    eventid: int
    seatid: str
    zone: str
    paymentid: int
    amount: int
    price: float
    tax: Optional[float] = 0

# Thai names and data
user_db = [
    UserOut(userid=1, username="somsak_ta", email="somsak.t@thaiemail.com"),
    UserOut(userid=2, username="jira_suk", email="jira.s@thaiemail.com"),
    UserOut(userid=3, username="wanida_nap", email="wanida.n@thaiemail.com"),
    UserOut(userid=4, username="krit_sara", email="krit.s@thaiemail.com"),
    UserOut(userid=5, username="naree_porn", email="naree.p@thaiemail.com"),
    UserOut(userid=6, username="phong_sri", email="phong.s@thaiemail.com"),
    UserOut(userid=7, username="supachai_t", email="supachai.t@thaiemail.com"),
    UserOut(userid=8, username="kanok_n", email="kanok.n@thaiemail.com"),
    UserOut(userid=9, username="chanya_nu", email="chanya.n@thaiemail.com"),
    UserOut(userid=10, username="ananda_j", email="ananda.j@thaiemail.com")
]


events_db = [
    Events(eventid=1, eventname="Summer Festival", venue="Impact Arena", eventdate="2025-07-10", available_tickets=5000),
    Events(eventid=2, eventname="Tech Conference", venue="Rajamangala National Stadium", eventdate="2025-08-15", available_tickets=2000),
    Events(eventid=3, eventname="Art Exhibition", venue="GMM Live House", eventdate="2025-09-20", available_tickets=1500),
    Events(eventid=4, eventname="Music Gala", venue="Impact Arena", eventdate="2025-10-05", available_tickets=3500),
    Events(eventid=5, eventname="Food Festival", venue="GMM Live House", eventdate="2025-11-12", available_tickets=4000),
    Events(eventid=6, eventname="Cultural Show", venue="Thunder Dome", eventdate="2025-12-01", available_tickets=3000),
    Events(eventid=7, eventname="Film Premiere", venue="Central World Arena", eventdate="2026-01-15", available_tickets=2500),
    Events(eventid=8, eventname="Sports Event", venue="Rajamangala National Stadium", eventdate="2026-02-20", available_tickets=5000),
    Events(eventid=9, eventname="Dance Performance", venue="Impact Arena", eventdate="2026-03-25", available_tickets=3500),
    Events(eventid=10, eventname="Business Expo", venue="GMM Live House", eventdate="2026-04-30", available_tickets=2000)
]

payments_db = [
    Payment(paymentid=1, status="Completed", PaymentMethod="Credit Card"),
    Payment(paymentid=2, status="Pending", PaymentMethod="PayPal"),
    Payment(paymentid=3, status="Failed", PaymentMethod="Bank Transfer"),
    Payment(paymentid=4, status="Completed", PaymentMethod="Debit Card"),
    Payment(paymentid=5, status="Refunded", PaymentMethod="Credit Card"),
    Payment(paymentid=6, status="Completed", PaymentMethod="Credit Card"),
    Payment(paymentid=7, status="Pending", PaymentMethod="PayPal"),
    Payment(paymentid=8, status="Failed", PaymentMethod="Bank Transfer"),
    Payment(paymentid=9, status="Completed", PaymentMethod="Debit Card"),
    Payment(paymentid=10, status="Refunded", PaymentMethod="Credit Card")
]

seats_db = [
    Seats(seatid=1, seatposition="A1", zone="Front"),
    Seats(seatid=2, seatposition="B15", zone="Middle"),
    Seats(seatid=3, seatposition="C30", zone="Back"),
    Seats(seatid=4, seatposition="D10", zone="VIP"),
    Seats(seatid=5, seatposition="E20", zone="Standard"),
    Seats(seatid=6, seatposition="F25", zone="Premium"),
    Seats(seatid=7, seatposition="G5", zone="Front"),
    Seats(seatid=8, seatposition="H18", zone="Middle"),
    Seats(seatid=9, seatposition="J12", zone="Back"),
    Seats(seatid=10, seatposition="K7", zone="VIP")
]

tickets_db = [
    Ticket(name="VIP Pass", description="Access to all areas", price=3000.0, tax=150.0, tags=["VIP", "Access"], pic="vip_pass.jpg"),
    Ticket(name="Standard Ticket", description="General admission", price=800.0, tax=40.0, tags=["standard"], pic="standard_ticket.jpg"),
    Ticket(name="Family Pack", description="4 tickets bundle", price=3000.0, tax=120.0, tags=["family", "bundle"], pic="family_pack.jpg"),
    Ticket(name="Early Bird Ticket", description="Discounted early purchase", price=600.0, tax=30.0, tags=["early bird"], pic="early_bird_ticket.jpg"),
    Ticket(name="Group Ticket", description="Tickets for groups of 10 or more", price=2500.0, tax=100.0, tags=["group"], pic="group_ticket.jpg"),
    Ticket(name="Student Ticket", description="Discounted for students", price=500.0, tax=25.0, tags=["student"], pic="student_ticket.jpg"),
    Ticket(name="Senior Ticket", description="Discounted for seniors", price=400.0, tax=20.0, tags=["senior"], pic="senior_ticket.jpg"),
    Ticket(name="Child Ticket", description="Discounted for children", price=300.0, tax=15.0, tags=["child"], pic="child_ticket.jpg"),
    Ticket(name="Family Premium", description="Premium family package", price=4000.0, tax=160.0, tags=["family", "premium"], pic="family_premium.jpg"),
    Ticket(name="Corporate Ticket", description="For corporate groups", price=3500.0, tax=140.0, tags=["corporate"], pic="corporate_ticket.jpg")
]

venues_db = [
    Venue(id=1, name="Impact Arena", capacity=20000),
    Venue(id=2, name="Rajamangala National Stadium", capacity=50000),
    Venue(id=3, name="GMM Live House", capacity=3000),
    Venue(id=4, name="Thunder Dome", capacity=10000),
    Venue(id=5, name="Central World Arena", capacity=7000),
    Venue(id=6, name="Queen Sirikit National Convention Center", capacity=15000),
    Venue(id=7, name="BITEC Bangna", capacity=20000),
    Venue(id=8, name="MCC Hall", capacity=5000),
    Venue(id=9, name="Siam Paragon Hall", capacity=4000),
    Venue(id=10, name="MBK Center", capacity=3000)
]

organizers_db = [
    Organizer(id=456, name="Event Corp", email="contact@eventcorp.com"),
    Organizer(id=457, name="TechMasters", email="info@techmasters.com"),
    Organizer(id=458, name="Art Group", email="hello@artgroup.com"),
    Organizer(id=459, name="Music Events", email="music@eventsmail.com"),
    Organizer(id=460, name="Festival Planners", email="info@festivalplanners.com"),
    Organizer(id=461, name="Cultural Shows", email="cultural@shows.com"),
    Organizer(id=462, name="Film Premieres", email="film@premieres.com"),
    Organizer(id=463, name="Sports Events", email="sports@events.com"),
    Organizer(id=464, name="Dance Productions", email="dance@productions.com"),
    Organizer(id=465, name="Business Expo Org", email="expo@org.com")
]

bookings_db = [
    Booking(bookingid=2999, userid=1, eventid=1, seatid="A1", zone="Front", paymentid=1, amount=2, price=6000.0, tax=300.0),
    Booking(bookingid=3000, userid=2, eventid=2, seatid="B15", zone="Middle", paymentid=2, amount=1, price=800.0, tax=40.0),
    Booking(bookingid=3001, userid=3, eventid=3, seatid="C30", zone="Back", paymentid=3, amount=4, price=3200.0, tax=160.0),
    Booking(bookingid=3002, userid=4, eventid=4, seatid="D10", zone="VIP", paymentid=4, amount=3, price=9000.0, tax=450.0),
    Booking(bookingid=3003, userid=5, eventid=5, seatid="E20", zone="Standard", paymentid=5, amount=2, price=1600.0, tax=80.0),
    Booking(bookingid=3004, userid=6, eventid=6, seatid="F25", zone="Premium", paymentid=6, amount=5, price=15000.0, tax=750.0),
    Booking(bookingid=3005, userid=7, eventid=7, seatid="G5", zone="Front", paymentid=7, amount=1, price=2500.0, tax=125.0),
    Booking(bookingid=3006, userid=8, eventid=8, seatid="H18", zone="Middle", paymentid=8, amount=3, price=2400.0, tax=120.0),
    Booking(bookingid=3007, userid=9, eventid=9, seatid="J12", zone="Back", paymentid=9, amount=2, price=1200.0, tax=60.0),
    Booking(bookingid=3008, userid=10, eventid=10, seatid="K7", zone="VIP", paymentid=10, amount=1, price=3500.0, tax=175.0)
]

@app.get("/user/", response_model=List[UserOut])
async def read_user():
    return user_db

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    new_user = UserOut(
        userid=len(user_db) + 1,
        username=user.username,
        email=user.email
    )
    user_db.append(new_user)
    print(f"Created user: {new_user}")
    return new_user

@app.put("/user/{userid}", response_model=UserOut)
async def update_user(userid: int, user: UserIn):
    for i, existing_user in enumerate(user_db):
        if existing_user.userid == userid:
            updated_user = UserOut(
                userid=userid,
                username=user.username,
                email=user.email
            )
            user_db[i] = updated_user
            return updated_user
    
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

@app.delete("/user/{userid}")
async def delete_user(userid: int):
    for i, user in enumerate(user_db):
        if user.userid == userid:
            user_db.pop(i)
            return {"message": "success"}
    
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )



@app.get("/events/", response_model=List[Events])
async def get_events():
    return events_db

@app.get("/payments/", response_model=List[Payment])
async def get_payments():
    return payments_db

@app.get("/seats/", response_model=List[Seats])
async def get_seats():
    return seats_db

@app.get("/tickets/", response_model=List[Ticket])
async def get_tickets():
    return tickets_db

@app.get("/venues/", response_model=List[Venue])
async def get_venues():
    return venues_db

@app.get("/organizers/", response_model=Union[List[Organizer], Organizer])
async def get_organizers(id:int=None):
    if id is None:
        return organizers_db
    else:
        for org in organizers_db:
            if org.id == id:
                return org
        raise HTTPException(status_code=404, detail="Organizer not found")
    
@app.get("/organizers/{id}", response_model=Organizer)
async def get_organizer_by_id(id: int):
    for org in organizers_db:
        if org.id == id:
            return org
    raise HTTPException(status_code=404, detail="Organizer not found")

            
@app.post("/organizers/", response_model=Organizer)
async def create_organizer(organizer:OrganizerAlter):
     
    new_organizer = Organizer(
        id= organizers_db[-1].id+1,
        **organizer.model_dump()
    )
    
    organizers_db.append(new_organizer)
    return new_organizer

@app.put("/organizers/{organizer_id}",response_model=Organizer)
async def update_item(organizer_id:int,organizer:OrganizerAlter):
    new_organizer = Organizer(
        id=organizer_id,
        **organizer.model_dump()
    )
    
    for i in range(len(organizers_db)):
        if organizers_db[i].id == organizer_id:
            organizers_db[i] = new_organizer
            break
        
    return new_organizer

@app.delete("/organizers/{organizer_id}")
async def delete_organizer(organizer_id: int):
    print(f"Delete organizer id {organizer_id}")
    
    for i in range(len(organizers_db)):
        if organizers_db[i].id == organizer_id:
            organizers_db.pop(i)
            return {"Message":"success"}

    raise HTTPException(
        status_code=404,
        detail="Organizer not found"
    )

@app.get("/bookings/", response_model=List[Booking])
async def get_bookings():
    return bookings_db

@app.get("/bookings/{bookingid}", response_model=Booking)
async def get_booking(bookingid: int):
    booking = next((booking for booking in bookings_db if booking.bookingid == bookingid), None)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@app.post("/bookings/", response_model=Booking)
async def create_booking(booking: Booking):
    booking.bookingid = max(b.bookingid for b in bookings_db) + 1  # Auto-increment ID
    bookings_db.append(booking)
    print(bookings_db)
    return booking

@app.put("/bookings/{bookingid}", response_model=Booking)
async def update_booking(bookingid: int, updated_booking: Booking):
    for i, booking in enumerate(bookings_db):
        if booking.bookingid == bookingid:
            updated_booking.bookingid = bookingid  # Ensure the ID remains unchanged
            bookings_db[i] = updated_booking
            return updated_booking
    raise HTTPException(status_code=404, detail="Booking not found")

@app.delete("/bookings/{bookingid}")
async def delete_booking(bookingid: int):
    for i, booking in enumerate(bookings_db):
        if booking.bookingid == bookingid:
            del bookings_db[i]
            return {"message": "Booking deleted successfully"}
    raise HTTPException(status_code=404, detail="Booking not found")

