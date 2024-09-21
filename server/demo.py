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

class Venue(BaseModel):
    id: int
    name: str
    capacity: int

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

class OrganizerAlter(BaseModel):
    name: str
    email: str

class Organizer(OrganizerAlter):
    id:int

class EventsAlter(BaseModel):
    eventname: str
    venue: str
    eventdate: str
    available_tickets: int

class Events(EventsAlter):
    eventid:int

class TicketAlter(BaseModel):
    name: str
    description: Optional[str] = ''
    price: float
    tax: Optional[float] = 0
    tags: List[str] = []
    pic: str

class Ticket(TicketAlter):
    id: int

class Payment(BaseModel):
    paymentid: int
    status: str
    PaymentMethod: str

class Seats(BaseModel):
    seatid: int
    seatposition: str
    zone: str
    price: float


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
    Events(eventid=1, eventname="BTS Live in Bangkok", venue="Impact Arena", eventdate="2025-07-10", available_tickets=5000),
    Events(eventid=2, eventname="Blackpink World Tour", venue="Rajamangala National Stadium", eventdate="2025-08-15", available_tickets=2000),
    Events(eventid=3, eventname="EXO Concert Experience", venue="GMM Live House", eventdate="2025-09-20", available_tickets=1500),
    Events(eventid=4, eventname="TWICE Fan Meeting", venue="Impact Arena", eventdate="2025-10-05", available_tickets=3500),
    Events(eventid=5, eventname="Red Velvet Live", venue="Impact Arena", eventdate="2025-11-12", available_tickets=4000),
    Events(eventid=6, eventname="NCT 127 Performance", venue="Thunder Dome", eventdate="2025-12-01", available_tickets=3000),
    Events(eventid=7, eventname="ATEEZ World Tour", venue="Central World Arena", eventdate="2026-01-15", available_tickets=2500),
    Events(eventid=8, eventname="ITZY Concert", venue="Rajamangala National Stadium", eventdate="2026-02-20", available_tickets=5000),
    Events(eventid=9, eventname="Stray Kids Live Show", venue="Impact Arena", eventdate="2026-03-25", available_tickets=3500),
    Events(eventid=10, eventname="GOT7 Fan Event", venue="GMM Live House", eventdate="2026-04-30", available_tickets=2000)
]


payments_db = [
    Payment(paymentid=1, status="Completed", PaymentMethod="PromptPay"),
    Payment(paymentid=2, status="Pending", PaymentMethod="TrueMoney"),
    Payment(paymentid=3, status="Failed", PaymentMethod="Bank Transfer"),
    Payment(paymentid=4, status="Completed", PaymentMethod="Credit Card"),
    Payment(paymentid=5, status="Refunded", PaymentMethod="PromptPay"),
    Payment(paymentid=6, status="Completed", PaymentMethod="Debit Card"),
    Payment(paymentid=7, status="Pending", PaymentMethod="TrueMoney"),
    Payment(paymentid=8, status="Failed", PaymentMethod="Bank Transfer"),
    Payment(paymentid=9, status="Completed", PaymentMethod="Credit Card"),
    Payment(paymentid=10, status="Refunded", PaymentMethod="Debit Card")
]


seats_db = [
    Seats(seatid=1, seatposition="A1", zone="A"),
    Seats(seatid=2, seatposition="B15", zone="B"),
    Seats(seatid=3, seatposition="C30", zone="C"),
    Seats(seatid=4, seatposition="D10", zone="D"),
    Seats(seatid=5, seatposition="E20", zone="E"),
    Seats(seatid=6, seatposition="F25", zone="F"),
    Seats(seatid=7, seatposition="G5", zone="G"),
    Seats(seatid=8, seatposition="H18", zone="H"),
    Seats(seatid=9, seatposition="J12", zone="J"),
    Seats(seatid=10, seatposition="K7", zone="K")
]

tickets_db = [
    Ticket(id=1, name="BLACKPINK World Tour - VIP", description="Access to VIP lounge, soundcheck, and premium seating", price=7500.0, tax=375.0, tags=["VIP", "K-Pop"], pic="blackpink_vip.jpg"),
    Ticket(id=2, name="BLACKPINK World Tour - General Admission", description="General admission for BLACKPINK concert", price=2500.0, tax=125.0, tags=["K-Pop", "General"], pic="blackpink_general.jpg"),
    Ticket(id=3, name="Coldplay Music of the Spheres Tour - Golden Circle", description="Front row seats at Coldplay’s concert", price=8000.0, tax=400.0, tags=["Golden Circle", "International"], pic="coldplay_golden_circle.jpg"),
    Ticket(id=4, name="Coldplay Music of the Spheres Tour - Early Bird", description="Discounted tickets for early buyers", price=5500.0, tax=275.0, tags=["Early Bird", "International"], pic="coldplay_early_bird.jpg"),
    Ticket(id=5, name="GMM Grammy Superstar Concert - Sponsor Pass", description="Exclusive entry with sponsor perks", price=0, tax=0, tags=["Sponsor", "Thai"], pic="gmm_sponsor.jpg"),
    Ticket(id=6, name="Jay Chou Carnival Tour - Group Package", description="Discount for groups of 5 or more", price=10000.0, tax=500.0, tags=["Mandopop", "Group"], pic="jaychou_group.jpg"),
    Ticket(id=7, name="Peck Palitchoke Live Show - Student Pass", description="Discounted tickets for students", price=1200.0, tax=60.0, tags=["Thai", "Student"], pic="peck_palitchoke_student.jpg"),
    Ticket(id=8, name="Ariana Grande Sweetener Tour - Senior Pass", description="Discounted tickets for seniors", price=2000.0, tax=100.0, tags=["Pop", "Senior"], pic="ariana_senior.jpg"),
    Ticket(id=9, name="The TOYS Live Concert - Child Ticket", description="Discounted entry for children", price=1000.0, tax=50.0, tags=["Thai", "Child"], pic="the_toys_child.jpg"),
    Ticket(id=10, name="Thailand Cultural Concert - Family Premium", description="Special premium family package", price=5000.0, tax=250.0, tags=["Thai", "Family"], pic="thai_culture_family.jpg"),
    Ticket(id=11, name="Billie Eilish Live in Bangkok - Corporate Package", description="Corporate ticketing option for groups", price=12000.0, tax=600.0, tags=["Corporate", "Pop"], pic="billie_eilish_corporate.jpg")
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
    Organizer(id=456, name="K-Pop Concerts Thailand", email="contact@kpopconcertsthailand.com"),
    Organizer(id=457, name="Big Hit Entertainment", email="info@bighitent.com"),
    Organizer(id=458, name="YG Entertainment", email="hello@ygent.com"),
    Organizer(id=459, name="SM Entertainment", email="music@sment.com"),
    Organizer(id=460, name="JYP Entertainment", email="info@jypent.com"),
    Organizer(id=461, name="Live Nation Thailand", email="cultural@livenation.com"),
    Organizer(id=462, name="GMM Grammy", email="film@gmmgrammy.com"),
    Organizer(id=463, name="Thai Ticket Major", email="sports@thaiticketmajor.com"),
    Organizer(id=464, name="BEC-Tero Entertainment", email="dance@bectero.com"),
    Organizer(id=465, name="M-Thailand", email="expo@mthailand.com")
]


bookings_db = bookings_db = [
    Booking(bookingid=2999, userid=1, eventid=1, seatid="A1", zone="A", paymentid=1, amount=2, price=6000.0, tax=300.0),
    Booking(bookingid=3000, userid=2, eventid=2, seatid="B15", zone="B", paymentid=2, amount=1, price=800.0, tax=40.0),
    Booking(bookingid=3001, userid=3, eventid=3, seatid="C30", zone="C", paymentid=3, amount=4, price=3200.0, tax=160.0),
    Booking(bookingid=3002, userid=4, eventid=4, seatid="D10", zone="D", paymentid=4, amount=3, price=9000.0, tax=450.0),
    Booking(bookingid=3003, userid=5, eventid=5, seatid="E20", zone="E", paymentid=5, amount=2, price=1600.0, tax=80.0),
    Booking(bookingid=3004, userid=6, eventid=6, seatid="F25", zone="F", paymentid=6, amount=5, price=15000.0, tax=750.0),
    Booking(bookingid=3005, userid=7, eventid=7, seatid="G5", zone="G", paymentid=7, amount=1, price=2500.0, tax=125.0),
    Booking(bookingid=3006, userid=8, eventid=8, seatid="H18", zone="H", paymentid=8, amount=3, price=2400.0, tax=120.0),
    Booking(bookingid=3007, userid=9, eventid=9, seatid="J12", zone="J", paymentid=9, amount=2, price=1200.0, tax=60.0),
    Booking(bookingid=3008, userid=10, eventid=10, seatid="K7", zone="K", paymentid=10, amount=1, price=3500.0, tax=175.0)
]



# Payments Endpoints
@app.get("/payments", response_model=list[Payment])
async def read_payments():
    return payments_db

@app.get("/payments/{paymentid}", response_model=Payment)
async def read_payment(paymentid: int):
    payment = next((payment for payment in payments_db if payment.paymentid == paymentid), None)
    if payment:
        return payment
    raise HTTPException(status_code=404, detail="Payment not found")

@app.post("/payments", response_model=Payment)
async def create_payment(payment: Payment):
    payments_db.append(payment)
    return payment

@app.put("/payments/{paymentid}", response_model=Payment)
async def update_payment(paymentid: int, payment: Payment):
    for i, existing_payment in enumerate(payments_db):
        if existing_payment.paymentid == paymentid:
            payments_db[i] = payment
            return payment
    raise HTTPException(status_code=404, detail="Payment not found")

@app.delete("/payments/{paymentid}")
async def delete_payment(paymentid: int):
    global payments_db
    payments_db = [payment for payment in payments_db if payment.paymentid != paymentid]
    return {"message": "Payment deleted successfully"}

# Events Endpoints
@app.get("/events/", response_model=list[Events])
async def get_events():
    return events_db

@app.get("/events/{eventid}", response_model=Events)
async def get_event(eventid: int):
    event = next((event for event in events_db if event.eventid == eventid), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.post("/events/", response_model=Events)
async def create_event(event: EventsAlter):
    new_event = Events(
        id=events_db[-1].eventid+1,
        **event.model_dump()
    )

    events_db.append(new_event)
    return new_event

@app.put("/events/{eventid}", response_model=Events)
async def update_event(eventid: int, updated_event: Events):
    for i, event in enumerate(events_db):
        if event.eventid == eventid:
            events_db[i] = updated_event
            return updated_event
    raise HTTPException(status_code=404, detail="Event not found")

@app.delete("/events/{eventid}", response_model=Events)
async def delete_event(eventid: int):
    for i, event in enumerate(events_db):
        if event.eventid == eventid:
            events_db.pop(i)
            return {"message": "Event deleted successfully"}
    raise HTTPException(status_code=404, detail="Event not found")


@app.get("/organizers/", response_model=Union[List[Organizer], Organizer])
async def get_organizers(id:int=None):
    if id is None:
        return organizers_db
    else:
        for org in organizers_db:
            if org.id == id:
                return org
        raise HTTPException(status_code=404, detail="Organizer not found")

@app.post("/organizers/", response_model=Organizer)
async def create_organizer(organizer: OrganizerAlter):
    new_organizer = Organizer(
        id=organizers_db[-1].id + 1,
        **organizer.model_dump()
    )
    organizers_db.append(new_organizer)
    return new_organizer

@app.put("/organizers/{organizer_id}", response_model=Organizer)
async def update_organizer(organizer_id: int, organizer: OrganizerAlter):
    for i, org in enumerate(organizers_db):
        if org.id == organizer_id:
            organizers_db[i] = Organizer(id=organizer_id, **organizer.model_dump())
            return organizers_db[i]
    raise HTTPException(status_code=404, detail="Organizer not found")

@app.delete("/organizers/{organizer_id}")
async def delete_organizer(organizer_id: int):
    for i, org in enumerate(organizers_db):
        if org.id == organizer_id:
            organizers_db.pop(i)
            return {"message": "Organizer deleted successfully"}
    raise HTTPException(status_code=404, detail="Organizer not found")



@app.get("/venues/", response_model=List[Venue])
async def get_venues():
    return venues_db

@app.get("/venues/{venue_id}", response_model=Venue)
async def get_venue(venue_id: int):
    venue = next((venue for venue in venues_db if venue.id == venue_id), None)
    if venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue

@app.post("/venues/", response_model=Venue)
async def create_venue(venue: Venue):
    venues_db.append(venue)
    return venue

@app.put("/venues/{venue_id}", response_model=Venue)
async def update_venue(venue_id: int, updated_venue: Venue):
    for i, venue in enumerate(venues_db):
        if venue.id == venue_id:
            venues_db[i] = updated_venue
            return updated_venue
    raise HTTPException(status_code=404, detail="Venue not found")

@app.delete("/venues/{venue_id}")
async def delete_venue(venue_id: int):
    for i, venue in enumerate(venues_db):
        if venue.id == venue_id:
            venues_db.pop(i)
            return {"message": "Venue deleted successfully"}
    raise HTTPException(status_code=404, detail="Venue not found")



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
    booking.bookingid = max(b.bookingid for b in bookings_db) + 1
    bookings_db.append(booking)
    return booking

@app.put("/bookings/{bookingid}", response_model=Booking)
async def update_booking(bookingid: int, updated_booking: Booking):
    for i, booking in enumerate(bookings_db):
        if booking.bookingid == bookingid:
            bookings_db[i] = updated_booking
            return updated_booking
    raise HTTPException(status_code=404, detail="Booking not found")

@app.delete("/bookings/{bookingid}")
async def delete_booking(bookingid: int):
    for i, booking in enumerate(bookings_db):
        if booking.bookingid == bookingid:
            bookings_db.pop(i)
            return {"message": "Booking deleted successfully"}
    raise HTTPException(status_code=404, detail="Booking not found")



@app.get("/users", response_model=list[UserOut])
async def read_users():
    return user_db

@app.get("/users/{userid}", response_model=UserOut)
async def read_user(userid: int):
    user = next((user for user in user_db if user.userid == userid), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users", response_model=UserOut)
async def create_user(user: UserIn):
    userid = max(u.userid for u in user_db) + 1
    new_user = UserOut(userid=userid, username=user.username, email=user.email)
    user_db.append(new_user)
    return new_user

@app.put("/users/{userid}", response_model=UserOut)
async def update_user(userid: int, user: UserIn):
    for i, existing_user in enumerate(user_db):
        if existing_user.userid == userid:
            updated_user = UserOut(userid=userid, username=user.username, email=user.email)
            user_db[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{userid}")
async def delete_user(userid: int):
    global user_db
    user_db = [user for user in user_db if user.userid != userid]
    return {"message": "User deleted successfully"}


@app.get("/seats/", response_model=List[Seats])
async def get_seats():
    return seats_db


@app.get("/seats/{seatid}", response_model=Seats)
async def get_seat(seatid: int):
    seat = next((seat for seat in seats_db if seat.seatid == seatid), None)
    if seat is None:
        raise HTTPException(status_code=404, detail="Seat not found")
    return seat

@app.post("/seats/", response_model=Seats)
async def create_seat(seat: Seats):
    if any(existing_seat.seatid == seat.seatid for existing_seat in seats_db):
        raise HTTPException(status_code=400, detail="Seat ID already exists")
    seats_db.append(seat)
    return seat

@app.put("/seats/{seatid}", response_model=Seats)
async def update_seat(seatid: int, updated_seat: Seats):
    for i, seat in enumerate(seats_db):
        if seat.seatid == seatid:
            updated_seat.seatid = seatid  # Ensure the seat ID remains unchanged
            seats_db[i] = updated_seat
            return updated_seat
    raise HTTPException(status_code=404, detail="Seat not found")

@app.delete("/seats/{seatid}")
async def delete_seat(seatid: int):
    for i, seat in enumerate(seats_db):
        if seat.seatid == seatid:
            del seats_db[i]
            return {"message": "Seat deleted successfully"}
    raise HTTPException(status_code=404, detail="Seat not found")

# Helper function to get the next ticket id

@app.get("/tickets/", response_model=List[Ticket])
async def get_tickets():
    return tickets_db

@app.get("/tickets/{ticket_id}", response_model=Ticket)
async def get_ticket(ticket_id: int):
    ticket = next((ticket for ticket in tickets_db if ticket.id == ticket_id), None)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

#@app.post("/tickets/", response_model=Ticket)
#async def create_ticket(ticket: TicketAlter):
    new_ticket = Ticket(
        id=tickets_db[-1].id+1,
        **ticket.model_dump()
    )
    tickets_db.append(new_ticket)
    return new_ticket

@app.post("/tickets/", response_model=Ticket)
async def create_ticket(ticket: Ticket):
    if any(t.id == ticket.id for t in tickets_db):
        raise HTTPException(status_code=400, detail="Ticket with this ID already exists")
    tickets_db.append(ticket)
    print(f"Created ticket: {ticket}")
    return ticket  


@app.put("/tickets/{ticket_id}", response_model=Ticket)
async def update_ticket(ticket_id: int, updated_ticket: Ticket):
    for i, ticket in enumerate(tickets_db):
        if ticket.id == ticket_id:
            updated_ticket.id = ticket_id  # Preserve the original id
            tickets_db[i] = updated_ticket
            return updated_ticket
    raise HTTPException(status_code=404, detail="Ticket not found")

@app.delete("/tickets/{ticket_id}")
async def delete_ticket(ticket_id: int):
    for i, ticket in enumerate(tickets_db):
        if ticket.id == ticket_id:
            del tickets_db[i]
            return {"message": "Ticket deleted successfully"}
    raise HTTPException(status_code=404, detail="Ticket not found")

