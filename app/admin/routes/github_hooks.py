# in routes/github_hooks.py
from flask import Blueprint, request, abort
import hmac
import hashlib
import subprocess
from app.admin import admin
import os

LOGFILE = "/tmp/github_webhook.log"  # you can view this later
GITHUB_SECRET = os.environ.get("GITHUB_SECRET", 'FAIL').encode()

def log(msg):
    with open(LOGFILE, "a") as f:
        f.write(msg + "\n")

@admin.route('/github-webhook', methods=['POST'])
def github_webhook():
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