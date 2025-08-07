from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_customers():
    return {"message": "This is the customers endpoint."}
