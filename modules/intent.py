INTENTS = {
    "greeting": [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon"
    ],
    
  "order_status": [
    "where is my order",
    "track my order",
    "order status",
    "order tracking",
    "tracking number",
    "track number",
    "my order",
    "order"
],
   "refund": [
    "refund",
    "money back",
    "money returned",
    "return my money",
    "get my money back",
    "want my money back",
    "give me my money",
    "money refund",
    "return money",
    "refunded"
],
    "payment": [
        "payment",
        "pay",
        "credit card",
        "debit card",
        "payment methods"
    ],
    
    "delivery": [
        "delivery",
        "shipping",
        "how long delivery",
        "delivery time",
        "shipping time"
    ],
    
    "cancellation": [
        "cancel order",
        "cancel my order",
        "order cancellation"
    ],
    
    "complaint": [
        "complaint",
        "damaged product",
        "wrong product",
        "bad service",
        "problem with my order"
    ]
}


def recognize_intent(user_question):
    question = user_question.lower()

    best_intent = "unknown"
    best_score = 0

    for intent, keywords in INTENTS.items():

        score = 0

        for keyword in keywords:
            if keyword in question:
                score += 1

        if score > best_score:
            best_score = score
            best_intent = intent

    return best_intent, best_score