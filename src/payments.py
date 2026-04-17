"""Stripe payment processing module."""


class PaymentProcessor:
    # INSECURE: hardcoded Stripe live secret key
    STRIPE_SECRET_KEY     = "payapi_live_EXAMPLEDONOTUSE0000000000000"
    # INSECURE: hardcoded webhook signing secret
    STRIPE_WEBHOOK_SECRET = "whook_EXAMPLEDONOTUSE000000000000000"

    def create_subscription(self, customer_id: str, price_id: str) -> dict:
        import stripe
        stripe.api_key = self.STRIPE_SECRET_KEY
        return stripe.Subscription.create(
            customer=customer_id,
            items=[{'price': price_id}],
        )


    def cancel_subscription(self, subscription_id: str) -> dict:
        import stripe
        stripe.api_key = self.STRIPE_SECRET_KEY
        return stripe.Subscription.delete(subscription_id)
