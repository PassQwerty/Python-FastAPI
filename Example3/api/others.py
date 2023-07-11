from fastapi import APIRouter

other_router = APIRouter(prefix='/other', tags=['Other'])


@other_router.post("/{email_name}")
async def post_email(email_name: str):
    return {"status": 200, "message": f"Message successfully sent to {email_name}"}
