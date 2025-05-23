# serve.py (w dexbot-server)

from flask import Flask, send_from_directory
import os

app = Flask(__name__)
RESULTS_DIR = os.path.join("data", "results")

@app.route("/results/")
def list_results():
    try:
        files = os.listdir(RESULTS_DIR)
        files = sorted([f for f in files if f.endswith(".csv")])
        return "<br>".join([f"<a href='/results/{f}'>{f}</a>" for f in files]) or "Brak plików"
    except Exception as e:
        return f"Błąd: {e}"

@app.route("/results/<filename>")
def get_result_file(filename):
    return send_from_directory(RESULTS_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)