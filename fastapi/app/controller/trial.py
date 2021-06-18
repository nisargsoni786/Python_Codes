from fastapi import APIRouter

router=APIRouter()

@router.get('/tri')
async def rr():
    return {"Message":"In router"}