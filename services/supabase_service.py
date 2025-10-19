from supabase import create_client, Client
from config import Config

def get_supabase_client() -> Client:
    return create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)

supabase = get_supabase_client()

def sign_up_user(email, password):
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        
        user = response.user
        if not user:
            return {"error": "Signup failed"}

        return {
            "id": user.id,
            "email": user.email,
            "created_at": str(user.created_at)
        }

    except Exception as e:
        return {"error": str(e)}
    
    
def sign_in_user(email: str, password: str):
    try:
        result = supabase.auth.sign_in_with_password({"email": email, "password": password})

        return {
            "session": result.session and result.session.model_dump(),
            "user": result.user and result.user.model_dump()
        }

    except Exception as e:
        return {"error": str(e)}
