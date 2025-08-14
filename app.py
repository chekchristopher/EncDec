from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "goldendeveloper369secretkey"


def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
    
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


@app.route("/", methods=["GET", "POST"])
def index():
    #Get history from session or create new one
    history = session.get("history", [])

    encrypted_text = ""
    decrypted_text = ""
    used_shift = None
    error = None

    if request.method == "POST":
        if "encrypt" in request.form:
            text = request.form["encrypt_text"]
            password = request.form["encrypt_password"]

            #if no password, generate random shift 
            if password.strip() == "":
                error = "You must enter a numeric key for encryption."
            else:
                try:
                    shift = int(password)
                except ValueError:
                    shift = 0
            
            used_shift = shift
            encrypted_text = caesar_encrypt(text, shift)
            history.append({"action": f"Encrypt(shift={shift})", "input": text, "output": encrypted_text})
        elif "decrypt" in request.form:
            text = request.form["decrypt_text"]
            password = request.form["decrypt_password"]
            if password.strip() == "":
                error = "Enter the same key used for encryption."
            else:
                try:
                    shift = int(password)
                    used_shift = shift
                    decrypted_text = caesar_decrypt(text, shift)
                    history.append({
                        "action": f"Decrypt(Shift={shift})", 
                        "input": text, 
                        "output": decrypted_text
                    })     
                except ValueError:
                    error = "Must be integers."
             
        elif "clear_history" in request.form:
            history = [] #empty history
            session["history"]= history
            return redirect(url_for("index"))
        
        #save updated history in session
        session["history"] = history
    
    return render_template(
        "index.html",
        encrypted=encrypted_text,
        decrypted=decrypted_text,
        history=history,
        shift_used=used_shift,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)