
from getpass import getpass

from sqlalchemy import func

from app.database.connection import SessionLocal
from app.entity.models.user import Users
from app.core.security import hash_password


db = SessionLocal()

try:
    school_id = int(input("Enter School ID: "))
    email = input("Enter user email: ").strip().lower()

    user = db.query(Users).filter(
        Users.school_id == school_id,
        func.lower(Users.email) == email,
    ).first()

    if user is None:
        print("User not found.")
    else:
        password = getpass("Enter new password: ")
        confirm_password = getpass("Confirm password: ")

        if password != confirm_password:
            print("Passwords do not match.")
        elif len(password) < 8:
            print("Password must contain at least 8 characters.")
        else:
            user.password_hash = hash_password(password)
            db.commit()
            print("Password updated successfully.")

except Exception:
    db.rollback()
    raise

finally:
    db.close()
