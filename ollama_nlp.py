import requests
import json
import re

def process_command(text):
    prompt = f"""
You are an English grocery billing assistant.

Rules:
- If the user wants to buy something → intent = "add"
- If the user asks total price → intent = "bill"
- If the user says exit → intent = "exit"
- Quantity must be INTEGER only
- Item must be a single grocery name
- Return ONLY valid JSON (no explanation)

Sentence: "{text}"

Format:
{{
 "intent":"",
 "item":"",
 "quantity":1
}}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        data = response.json()
        output = data.get("response", "{}")

        print("RAW RESPONSE:", output)

        # Extract JSON safely
        match = re.search(r'\{.*\}', output, re.S)
        if not match:
            return {"intent": "unknown", "item": "", "quantity": 1}

        result = json.loads(match.group())

        # Ensure quantity is integer
        qty_match = re.search(r'\d+', str(result.get("quantity", 1)))
        result["quantity"] = int(qty_match.group()) if qty_match else 1

        return result

    except Exception as e:
        print("Ollama Error:", e)
        return {"intent": "unknown", "item": "", "quantity": 1}
