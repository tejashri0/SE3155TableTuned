from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_reviews():
    return {"message": "This is the review endpoint."}
