import re


def generate_context_response(
    user_question,
    history,
    faq_answer,
    language="English"
):

    question = user_question.lower()

    previous_messages = " ".join(
        message["content"].lower()
        for message in history
    )


    # =========================
    # TRACKING NUMBER
    # =========================

    tracking_match = re.search(
        r"\b\d{5,}\b",
        user_question
    )

    if tracking_match and (
        "tracking" in question
        or "track" in question
        or "order" in question
    ):

        tracking_number = tracking_match.group()

        if language == "Urdu":

            return (
                f"Shukriya! Mujhe aap ka tracking number "
                f"**{tracking_number}** mil gaya hai. "
                f"Hum is number ko aap ke order ka status "
                f"check karne ke liye use kar sakte hain."
            )

        else:

            return (
                f"Thanks! I received your tracking number: "
                f"**{tracking_number}**. "
                f"We can use this number to check your "
                f"order status."
            )


    # =========================
    # GREETING
    # =========================

    if any(
        word in question
        for word in ["hello", "hi", "hey"]
    ):

        if language == "Urdu":

            return (
                "Assalam-o-Alaikum! 👋 "
                "Hamari customer support mein khush aamdeed. "
                "Main aaj aapki kis tarah madad kar sakta hoon?"
            )

        else:

            return (
                "Hello! 👋 Welcome to our customer support. "
                "How can I help you today?"
            )


    # =========================
    # ORDER + TRACKING
    # =========================

    if (
        "order" in previous_messages
        and "tracking" in question
    ):

        if language == "Urdu":

            return (
                "Bilkul! Meharbani karke apna tracking number "
                "provide karein taake main aapke order ka "
                "status check karne mein madad kar sakoon."
            )

        else:

            return (
                "Sure! Please provide your tracking number "
                "so I can help you with your order status."
            )


    # =========================
    # FAQ RESPONSE
    # =========================

    if faq_answer:

        faq_response = faq_answer["answer"]


        if language == "Urdu":

            translations = {

                "You can track your order using your tracking number.":
                    "Aap apne tracking number ki madad se apne order ko track kar sakte hain.",

                "Orders can be cancelled before they are shipped.":
                    "Orders ko ship hone se pehle cancel kiya ja sakta hai.",

                "Refunds are usually processed within 5-7 business days.":
                    "Refund aam tor par 5 se 7 working days mein process hota hai.",

                "You can pay using credit card, debit card, or cash on delivery.":
                    "Aap credit card, debit card ya cash on delivery ke zariye payment kar sakte hain.",

                "Delivery usually takes 3-5 business days.":
                    "Delivery aam tor par 3 se 5 working days leti hai."
            }


            return translations.get(
                faq_response,
                "Aapke sawal ka jawab: " + faq_response
            )


        else:

            return faq_response


    # =========================
    # DEFAULT RESPONSE
    # =========================

    if language == "Urdu":

        return (
            "Maazrat, mujhe aapka sawal samajhne mein "
            "mushkil ho rahi hai. Barah-e-karam thori "
            "mazeed tafseel provide karein."
        )

    else:

        return (
            "I'm sorry, I couldn't understand your question. "
            "Could you please provide more details?"
        )