from fastapi import APIRouter

from .payment import api_router as payment_router

router = APIRouter()
router.include_router(payment_router)
