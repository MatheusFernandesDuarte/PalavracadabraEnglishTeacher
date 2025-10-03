from fastapi import APIRouter, Query

from app.services.word_service import get_random_word

router: APIRouter = APIRouter()


@router.get("/random", tags=["words"])
async def random_word(level: int = Query(1, ge=1, le=10)):
    return get_random_word(level=level)
