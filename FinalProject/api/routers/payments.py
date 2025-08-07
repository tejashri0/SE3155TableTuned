from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_payments():
    return {"message": "This is the payments endpoint."}
