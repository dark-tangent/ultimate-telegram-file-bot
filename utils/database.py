import os
from pymongo import MongoClient
from datetime import datetime

client = MongoClient(os.getenv("MONGO_URI"))
db = client["bot_database"]
users = db["users"]

def init_db():
    pass

def get_user(user_id):
    user = users.find_one({"_id": str(user_id)})
    if not user:
        user = {
            "_id": str(user_id),
            "is_premium": False,
            "used_today": 0,
            "daily_limit": 500 * 1024 * 1024,
            "last_reset": datetime.utcnow().date().isoformat(),
            "total_files_uploaded": 0,
            "total_bytes_uploaded": 0
        }
        users.insert_one(user)
    return user

def reset_daily_quota_if_needed(user_id):
    user = get_user(user_id)
    today = datetime.utcnow().date().isoformat()
    if user["last_reset"] != today:
        users.update_one({"_id": str(user_id)}, {"$set": {"used_today": 0, "last_reset": today}})

def update_user_usage(user_id, bytes_uploaded):
    users.update_one(
        {"_id": str(user_id)},
        {"$inc": {"used_today": bytes_uploaded, "total_files_uploaded": 1, "total_bytes_uploaded": bytes_uploaded}}
    )

def promote_user_to_premium(user_id):
    users.update_one({"_id": str(user_id)}, {"$set": {"is_premium": True, "daily_limit": 50 * 1024 * 1024 * 1024}})

def get_total_stats():
    total_users = users.count_documents({})
    total_uploaded = sum(user.get('total_bytes_uploaded', 0) for user in users.find())
    return total_users, total_uploaded