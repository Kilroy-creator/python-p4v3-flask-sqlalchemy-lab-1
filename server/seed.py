#!/usr/bin/env python3
from app import app, db, Earthquake

with app.app_context():
    # Clear existing data
    db.session.query(Earthquake).delete()
    
    # Add earthquakes
    db.session.add(Earthquake(magnitude=9.5, location="Chile", year=1960))
    db.session.add(Earthquake(magnitude=9.2, location="Alaska", year=1964))
    db.session.add(Earthquake(magnitude=8.6, location="Alaska", year=1946))
    db.session.add(Earthquake(magnitude=8.5, location="Banda Sea", year=1934))
    db.session.add(Earthquake(magnitude=8.4, location="Chile", year=1922))

    db.session.commit()
    
    print("Database seeded successfully!")