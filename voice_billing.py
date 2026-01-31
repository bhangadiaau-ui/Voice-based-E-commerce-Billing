import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

products = {
    "rice": 50,
    "sugar": 40,
    "milk": 30,
    "bread": 25,
    "apple": 60,
    "banana": 20
}

cart = {}
total = 0

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        speak("Sorry, I didn't understand.")
        return ""

speak("Voice billing started. Say item and quantity. Say total to finish.")

while True:
    text = listen()

    if "total" in text:
        break

    words = text.split()
    qty = 1
    item = None

    for w in words:
        if w.isdigit():
            qty = int(w)

    for p in products:
        if p in text:
            item = p
            break

    if item:
        cost = products[item] * qty
        total += cost
        cart[item] = cart.get(item, 0) + qty
        speak(f"Added {qty} {item}. Cost {cost} rupees")
    else:
        speak("Item not found")

print("\n----- FINAL BILL -----")

for item, qty in cart.items():
    cost = products[item] * qty
    print(f"{item} x {qty} = {cost}")
    speak(f"{item} {qty} cost {cost}")

print("Total =", total)
speak(f"Total amount is {total} rupees")
