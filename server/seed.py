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

    sample_requests = [
        ("ABC Mechanical", "123 Main Street, Yonkers, NY", "Ignitor, gasket kit", "2026-05-01", "Normal", "Requested"),
        ("City Hospital", "500 Park Avenue, New York, NY", "Gas valve", "2026-05-03", "Urgent", "In Progress"),
        ("Main Street Apartments", "75 Main Street, White Plains, NY", "Pressure switch, tubing", "2026-05-05", "Normal", "Ready"),
        ("Yonkers School District", "100 School Road, Yonkers, NY", "Burner gasket, flame sensor", "2026-05-07", "Low", "Completed"),
        ("Hudson Valley Mall", "200 Retail Drive, Nanuet, NY", "Control board", "2026-05-08", "Urgent", "Requested"),
        ("Northside Apartments", "44 North Ave, New Rochelle, NY", "Circulator pump", "2026-05-09", "Normal", "In Progress"),
        ("Riverside Towers", "88 River Road, Bronx, NY", "Aquastat", "2026-05-10", "Normal", "Requested"),
        ("Westchester Medical", "12 Hospital Way, Valhalla, NY", "Flame rod", "2026-05-11", "Urgent", "Ready"),
        ("Park Lane Condos", "19 Park Lane, Scarsdale, NY", "Expansion tank", "2026-05-12", "Low", "Requested"),
        ("Bronx Courthouse", "851 Grand Concourse, Bronx, NY", "Pilot assembly", "2026-05-13", "Urgent", "In Progress"),
        ("Greenview Estates", "33 Greenview Road, Tarrytown, NY", "Relief valve", "2026-05-14", "Normal", "Completed"),
        ("Metro Storage", "71 Warehouse Blvd, Mount Vernon, NY", "Transformer", "2026-05-15", "Low", "Requested"),
        ("Harbor Point", "9 Harbor Street, Stamford, CT", "Gas pressure switch", "2026-05-16", "Normal", "Ready"),
        ("Summit Office Park", "400 Summit Ave, White Plains, NY", "Combustion blower", "2026-05-17", "Urgent", "Requested"),
        ("Cedar Ridge Homes", "22 Cedar Road, Ossining, NY", "Rollout switch", "2026-05-18", "Normal", "In Progress"),
        ("East Gate Plaza", "111 East Gate Dr, Queens, NY", "Thermostat kit", "2026-05-19", "Low", "Requested"),
        ("Liberty Towers", "300 Liberty St, Jersey City, NJ", "Low water cutoff", "2026-05-20", "Urgent", "Ready"),
        ("Hillcrest School", "82 Hillcrest Ave, Yonkers, NY", "Sensor kit", "2026-05-21", "Normal", "Completed"),
        ("Union Mechanical", "57 Industrial Pkwy, Brooklyn, NY", "Actuator", "2026-05-22", "Normal", "Requested"),
        ("Oakwood Gardens", "66 Oakwood Dr, Dobbs Ferry, NY", "Pump seal kit", "2026-05-23", "Low", "In Progress"),
    ]

    requests = []

    for i, item in enumerate(sample_requests):
        job_name, address, parts_requested, date_needed, priority, status = item

        new_request = Request(
            job_name=job_name,
            address=address,
            parts_requested=parts_requested,
            date_needed=date_needed,
            priority=priority,
            status=status,
            user_id=user1.id if i % 2 == 0 else user2.id
        )

        requests.append(new_request)

    db.session.add_all(requests)
    db.session.commit()

    print("Creating updates...")

    update1 = Update(
        message="Request submitted by technician.",
        user_id=user2.id,
        request_id=requests[0].id
    )

    update2 = Update(
        message="Parts team is reviewing availability.",
        user_id=user1.id,
        request_id=requests[0].id
    )

    update3 = Update(
        message="Gas valve located. Preparing for pickup.",
        user_id=user1.id,
        request_id=requests[1].id
    )

    update4 = Update(
        message="Warehouse has started pulling parts.",
        user_id=user3.id,
        request_id=requests[1].id
    )

    update5 = Update(
        message="Parts staged on hold shelf.",
        user_id=user3.id,
        request_id=requests[2].id
    )

    update6 = Update(
        message="Request completed and picked up.",
        user_id=user3.id,
        request_id=requests[3].id
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