from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_recipes():
    return {"message": "This is the recipes endpoint."}
