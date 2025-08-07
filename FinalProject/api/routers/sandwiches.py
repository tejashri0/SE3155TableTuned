from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_sandwiches():
    return {"message": "This is the sandwiches endpoint."}
