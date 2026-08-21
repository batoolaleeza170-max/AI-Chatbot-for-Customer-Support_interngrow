def calculate_confidence(score):
    percentage = score * 100

    if percentage >= 80:
        level = "High"
        emoji = "🟢"

    elif percentage >= 50:
        level = "Medium"
        emoji = "🟡"

    else:
        level = "Low"
        emoji = "🔴"

    return percentage, level, emoji