from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Goal, UserProfile

dashboard_bp = Blueprint("dashboard", __name__)

# ==================================================
# 1️⃣ CREATE / UPDATE SAVED GOAL (REAL GOAL)
# ==================================================
@dashboard_bp.route("/goal", methods=["POST"])
@jwt_required()
def create_or_update_goal():
    data = request.json
    user_id = get_jwt_identity()

    plan_type = data.get("plan_type")   # monthly / yearly
    target_amount = data.get("target_amount")

    if plan_type not in ["monthly", "yearly"]:
        return {"error": "Invalid plan type"}, 400

    if not isinstance(target_amount, int) or target_amount <= 0:
        return {"error": "Invalid target amount"}, 400

    # Normalize to monthly
    normalized_monthly = (
        target_amount if plan_type == "monthly" else target_amount // 12
    )

    goal = Goal.query.filter_by(user_id=user_id).first()

    if goal:
        goal.plan_type = plan_type
        goal.target_amount = target_amount
        goal.normalized_monthly_amount = normalized_monthly
    else:
        goal = Goal(
            user_id=user_id,
            plan_type=plan_type,
            target_amount=target_amount,
            normalized_monthly_amount=normalized_monthly
        )
        db.session.add(goal)

    db.session.commit()

    return {
        "message": "Goal saved successfully",
        "plan_type": plan_type,
        "target_amount": target_amount,
        "monthly_target": normalized_monthly
    }, 200


# ==================================================
# 2️⃣ DASHBOARD OVERVIEW (ENTRY POINT)
# ==================================================
@dashboard_bp.route("/overview", methods=["GET"])
@jwt_required()
def dashboard_overview():
    user_id = get_jwt_identity()

    profile = UserProfile.query.filter_by(user_id=user_id).first()
    goal = Goal.query.filter_by(user_id=user_id).first()

    # Profile mandatory
    if not profile:
        return {
            "redirect": "profile_setup",
            "message": "Complete profile setup to continue"
        }, 200

    # Profile done, goal not set
    if not goal:
        return {
            "redirect": "set_goal",
            "profile_ready": True,
            "goal_set": False
        }, 200

    # Profile + goal done
    return {
        "redirect": "dashboard",
        "profile_ready": True,
        "goal_set": True,
        "current_goal": {
            "plan_type": goal.plan_type,
            "target_amount": goal.target_amount,
            "monthly_target": goal.normalized_monthly_amount
        }
    }, 200


# ==================================================
# 3️⃣ ESTIMATION MODE (WHAT-IF / EXCLAMATION MODE)
# DOES NOT SAVE TO DB
# ==================================================
@dashboard_bp.route("/estimate", methods=["POST"])
@jwt_required()
def estimate_goal():
    data = request.json
    user_id = get_jwt_identity()

    profile = UserProfile.query.filter_by(user_id=user_id).first()
    if not profile:
        return {"error": "Profile not completed"}, 400

    plan_type = data.get("plan_type")     # monthly / yearly
    amount = data.get("amount")

    if plan_type not in ["monthly", "yearly"]:
        return {"error": "Invalid plan type"}, 400

    if not isinstance(amount, int) or amount <= 0:
        return {"error": "Invalid amount"}, 400

    normalized_monthly = amount if plan_type == "monthly" else amount // 12

    return {
        "mode": "estimation",
        "message": "This is an estimated plan. It does not change your saved goal.",
        "plan_type": plan_type,
        "entered_amount": amount,
        "monthly_target": normalized_monthly,
        "next_step": "action_selection"
    }, 200
