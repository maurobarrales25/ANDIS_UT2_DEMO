from app.database.database import get_conn
from app.schema.user import UserCreate

class UserRepository:
    def get_all_users(self):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email FROM users")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_user_by_id(self, id: int):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email FROM users WHERE id = %s", (id,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user

    def save(self, user: UserCreate):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s, %s) RETURNING id",
            (user.name, user.email)
        )
        new_id = cur.fetchone()["id"]
        conn.commit()
        cur.close()
        conn.close()
        return {**user.dict(), "id": new_id}