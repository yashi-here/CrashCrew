from app import app
from models import db, ActionMaster

actions = [
    # -------- TRANSPORT --------
    ("Switch Petrol Car to EV (1,000km/mo)", "transport", 140, 8000, 168),
    ("Switch Petrol Bike to Electric (600km/mo)", "transport", 55, 1400, 66),
    ("Carpool with 3 colleagues (Daily)", "transport", 40, 2500, 48),
    ("Use Metro/Bus instead of Car", "transport", 110, 6000, 132),
    ("Bicycle for short trips (<3km)", "transport", 12, 400, 14),
    ("Walking instead of Auto (10km/week)", "transport", 8, 300, 10),
    ("Switch off engine at Red Lights", "transport", 4, 150, 5),
    ("Maintain correct Tire Pressure", "transport", 3, 200, 4),
    ("Cancel 1 Domestic Flight (pro-rata)", "transport", 25, 1000, 30),
    ("Drive in correct gear (Manual)", "transport", 5, 250, 6),

    # -------- ENERGY --------
    ("Install Rooftop Solar (3kW)", "energy", 246, 2500, 295),
    ("Switch AC to 26°C (from 22°C)", "energy", 35, 600, 42),
    ("Replace 5 Halogens with LEDs", "energy", 15, 250, 18),
    ("Use 5-Star Rated AC/Fridge", "energy", 20, 400, 24),
    ("Unplug Idle Gadgets", "energy", 6, 100, 7),
    ("Defrost Fridge regularly", "energy", 4, 80, 5),
    ("Sun-dry clothes (No Dryer)", "energy", 12, 200, 14),
    ("Use Solar Water Heater", "energy", 30, 500, 36),

    # -------- FOOD --------
    ("Switch to Vegan Diet", "food", 150, 1500, 180),
    ("Switch to Vegetarian Diet", "food", 60, 800, 72),
    ("Zero Food Waste (Planning meals)", "food", 15, 1200, 18),
    ("Grow own Kitchen Garden", "food", 5, 300, 6),
    ("Eat Local / Seasonal", "food", 10, 400, 12),
    ("Use Pressure Cooker", "food", 8, 120, 10),
    ("Include Millets in 1 meal daily", "food", 4, 50, 5),

    # -------- WATER & WASTE --------
    ("Avoid Bottled Water", "water", 6, 450, 7),
    ("Compost Organic Waste", "waste", 12, 100, 14),
    ("Reuse RO Waste Water", "water", 5, 50, 6),
    ("Install Low-flow Showerheads", "water", 4, 40, 5),
    ("Bucket Bath (vs Shower)", "water", 10, 80, 12),
    ("Fix Leaking Taps", "water", 3, 30, 4),
    ("Rainwater Harvesting", "water", 8, 100, 10),

    # -------- LIFESTYLE --------
    ("Carry Cloth Bag", "lifestyle", 2, 20, 2),
    ("Reuse Glass Containers", "lifestyle", 1.5, 50, 2),
    ("Segregate Dry/Wet waste", "waste", 2, 20, 2),
    ("Donate/Sell E-waste", "waste", 5, 200, 6),
    ("Double Clothing Lifespan", "lifestyle", 20, 1500, 24),
    ("Shop Second-hand (Thrifting)", "lifestyle", 25, 2000, 30),
    ("Digital Bills only", "lifestyle", 0.5, 0, 1),
    ("Bamboo Toothbrush / Neem Comb", "lifestyle", 0.5, -20, 1),
    ("Plant 1 Tree/month", "lifestyle", 2, 0, 2)
]

with app.app_context():
    for a in actions:
        db.session.add(
            ActionMaster(
                action_name=a[0],
                category=a[1],
                co2_saved_per_month=a[2],
                monthly_savings=a[3],
                credit_value=a[4]
            )
        )

    db.session.commit()

print("ActionMaster seeded successfully")
