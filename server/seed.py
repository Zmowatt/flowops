from app import app
from models import db, User, Request, Update

with app.app_context():

    print("Creating database...")

    Update.query.delete()
    Request.query.delete()
    User.query.delete()

    print("Creating users...")

    user1 = User(
        name="Zachary Mowatt",
        email="zmowatt@company.com",
        role="Admin",
    )
    user1.password_hash = "password123"

    user2 = User(
        name="Marco Volpe",
        email="mvolpe@company.com",
        role="Requester",
    )
    user2.password_hash = "wordpass123"

    user3 = User(
        name="Destiny Morales",
        email="dmorales@company.com",
        role="Fulfillment",
    )
    user3.password_hash = "mypassword123"

    db.session.add_all([user1, user2, user3])
    db.session.commit()

    print("Creating requests...")

    request1 = Request(
        job_name="ABC Mechanical",
        address="123 Main Street, New York, NY",
        parts_requested="Gasket kit",
        date_needed="2026-05-01",
        priority="Normal",
        status="Requested",
        user_id=user2.id
    )

    request2 = Request(
        job_name="City Hospital",
        address="500 Park Avenue, Queens, NY",
        parts_requested="Actuator",
        date_needed="2026-05-05",
        priority="Urgent",
        status="Ready",
        user_id=user1.id
    )

    request3 = Request(
        job_name="Yonkers High School",
        address="100 School Road, Yonkers, NY",
        parts_requested="Gas valve",
        date_needed="2026-06-10",
        priority="Low",
        status="In Progress",
        user_id=user3.id
    )

    request4 = Request(
        job_name="Uptown Apartments",
        address="75 Main Street, White Plains, NY",
        parts_requested="Pressure switch, Tubing",
        date_needed="2026-03-06",
        priority="Normal",
        status="Complete",
        user_id=user1.id
    )

    db.session.add_all([request1, request2, request3, request4])
    db.session.commit()

    print("Creating updates...")

    update1 = Update(
        message="Request submitted by technician.",
        user_id=user2.id,
        request_id=request1.id
    )

    update2 = Update(
        message="Parts team is reviewing availability.",
        user_id=user1.id,
        request_id=request1.id
    )

    update3 = Update(
        message="Gas valve located. Preparing for pickup.",
        user_id=user1.id,
        request_id=request2.id
    )

    update4 = Update(
        message="Warehouse has started pulling parts.",
        user_id=user3.id,
        request_id=request2.id
    )

    update5 = Update(
        message="Parts staged on hold shelf.",
        user_id=user3.id,
        request_id=request3.id
    )

    update6 = Update(
        message="Request completed and picked up.",
        user_id=user3.id,
        request_id=request4.id
    )

    db.session.add_all([
        update1,
        update2,
        update3,
        update4,
        update5,
        update6
    ])

    db.session.commit()

    print("Database seeded successfully.")