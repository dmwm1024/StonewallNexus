

from flask import request
from app.github import github_bp
import os

def log(msg):
    LOGFILE = "/tmp/github_webhook.log"  # you can view this later
    with open(LOGFILE, "a") as f:
        f.write(msg + "\n")

@github_bp.route('/github-webhook', methods=['POST'])
def github_webhook():
    GITHUB_SECRET = os.environ.get("GITHUB_SECRET", 'FAIL').encode()

    log("🔔 Webhook route hit!")

    # Print headers for visibility
    log("Headers:")
    for k, v in request.headers.items():
        log(f"{k}: {v}")

    # Print body length
    log(f"Payload size: {len(request.data)} bytes")

    # Just confirm it ran — skip signature for now
    log("✅ Route completed.")
    return "Ping", 200
