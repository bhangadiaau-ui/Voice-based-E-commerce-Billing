from stt import listen
from ollama_nlp import process_command
from cart import add_item, generate_bill, products
from tts import speak

while True:
    text = listen()

    if text == "":
        continue

    data = process_command(text)

    intent = data["intent"]
    item = data["item"]
    qty = data["quantity"]

    # ---------- ADD ----------
    if intent == "add":
        if item not in products:
            speak("Item not found in store")
            print("Invalid item:", item)
            continue

        add_item(item, qty)
        speak(f"{qty} {item} added")

    # ---------- BILL ----------
    elif intent == "bill":
        total = generate_bill()
        speak(f"Your total bill is {total}")

    # ---------- EXIT ----------
    elif intent == "exit":
        speak("Thank you")
        break
