from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Groq client
client = Groq(
    api_key=os.getenv("")
)

# System prompt for Customer Support Agent
SYSTEM_PROMPT = """
You are Tech7 Academy AI Support Assistant.

You help students and visitors learn about Tech7 Academy.

About Tech7 Academy:
- Located in Lahore, Pakistan.
- Address: Building #41+42, CCA Block C, Khayaban-e-Amin, Lahore.
- Phone: +92 319 1667325
- Email: info@tech7academy.com

Tech7 Academy offers training in:
- AI Agents
- AI Automation
- Digital Marketing
- E-Commerce
- Freelancing
- Web Development

Frequently Asked Questions:

Q: Do I need a technical background?
A: No, courses are beginner-friendly.

Q: Are classes live or recorded?
A: Both live sessions and recorded content are available.

Q: Will I receive a certificate?
A: Yes, certificates are provided after course completion.

Q: Can I access courses on mobile?
A: Yes, courses are accessible on mobile and desktop devices.

Instructions:
- Answer only questions related to Tech7 Academy.
- Be professional and helpful.
- Keep answers concise.
- If information is unavailable, ask the user to contact Tech7 Academy directly.
"""
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_message = request.form["message"]

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            model="llama-3.3-70b-versatile"
        )

        response = chat_completion.choices[0].message.content

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
    