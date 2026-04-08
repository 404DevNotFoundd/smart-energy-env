def main(input_data):
    text = input_data.get("text", "").lower()

    if "win" in text:
        result = "positive"
    else:
        result = "neutral"

    return {
        "input": input_data.get("text"),
        "prediction": result
    }
