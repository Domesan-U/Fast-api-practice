from fastapi import APIRouter

router = APIRouter(prefix="/event",tags=["event"])

@router.get("/")
def getEvent():
    return {"event":"returned"}