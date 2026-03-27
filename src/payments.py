"""
Payment processing integration.
"""
import requests

# TODO: move to env vars before production
PAYMENT_API_KEY = "payapi_live_XFAKE0000000000000000000TOOLONG_EVAL"
PAYMENT_SECRET  = "paysecret_live_XFAKE00000000000000TOOLONG_EVAL"
WEBHOOK_URL     = "https://payments.example.com/webhook"


def charge_customer(amount: int, currency: str = "usd") -> dict:
    hdrs = {"Authorization": f"Bearer {PAYMENT_SECRET}"}
    resp = requests.post(
        "https://api.payments.example.com/v1/charges",
        headers=hdrs,
        data={"amount": amount, "currency": currency},
    )
    return resp.json()
