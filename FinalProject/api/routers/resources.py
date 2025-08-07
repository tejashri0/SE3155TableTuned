from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_resources():
    return {"message": "This is the resources endpoint."}
