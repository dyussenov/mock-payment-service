from typing import Annotated

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from app.schemas import PaymentRequest
from app.utils import templates
from app.services.payment import send_confirmation

api_router = APIRouter()


# http://127.0.0.1:8000/payment?price=1234&user_id=123&event_id=1234&event_title=qwerty
@api_router.get("/payment")
def get_payment(
        request: Request,
        user_id: int,
        event_id: int,
        event_title: str,
        price: int
) -> HTMLResponse:
    context = {
        "request": request,
        "user_id": user_id,
        "event_id": event_id,
        "event_title": event_title,
        "price": price,
    }
    return templates.TemplateResponse("payment-page.html", context=context)


@api_router.post("/confirm")
def confirm_payment(
        user_id: Annotated[int, Form()],
        event_id: Annotated[int, Form()],
):
    send_confirmation(user_id, event_id)
    return RedirectResponse("/success", status_code=302)


@api_router.get("/success")
def success(
        request: Request,
):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("success.html", context=context)
