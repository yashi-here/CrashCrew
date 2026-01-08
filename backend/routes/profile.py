from flask import Blueprint, request, jsonify
from models import db, UserProfile

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/create", methods=["POST"])
def create_profile():
    data = request.json

    user_id = data.get("user_id")  # from register response

    if not user_id:
        return {"error": "user_id is required"}, 400

    # Prevent duplicate profile
    if UserProfile.query.filter_by(user_id=user_id).first():
        return {"error": "Profile already exists"}, 409

    profile = UserProfile(
        user_id=user_id,

        # Housing & Living
        living_arrangement=data.get("living_arrangement"),
        pays_electricity=data.get("pays_electricity"),
        household_size=data.get("household_size"),

        # Energy
        uses_ac=data.get("uses_ac"),
        appliances_used=",".join(data.get("appliances_used", [])),

        # Transportation
        primary_transport=data.get("primary_transport"),
        owns_vehicle=data.get("owns_vehicle"),

        # Food
        diet_type=data.get("diet_type"),
        eating_out_frequency=data.get("eating_out_frequency"),

        # Life stage & sustainability
        life_stage=data.get("life_stage"),
        sustainability_interest=data.get("sustainability_interest")
    )

    db.session.add(profile)
    db.session.commit()

    return {
        "message": "Profile created successfully",
        "next_step": "login"
    }, 201
