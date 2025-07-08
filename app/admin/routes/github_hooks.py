# in routes/github_hooks.py
from flask import Blueprint, request, abort
import hmac
import hashlib
import subprocess
from app.admin import admin
import os

LOGFILE = "/tmp/github_webhook.log"  # you can view this later
GITHUB_SECRET = os.environ.get("GITHUB_SECRET", 'FAIL').encode()

def log(message):
    with open(LOGFILE, "a") as f:
        f.write(message + "\n")

@admin.route('/github-webhook', methods=['POST'])
def github_webhook():
    log("🔔 Webhook hit!")

    signature = request.headers.get("X-Hub-Signature-256")
    if not signature:
        log("❌ Missing signature header.")
        abort(401)

    try:
        sha_name, signature_hash = signature.split("=")
        if sha_name != "sha256":
            log(f"❌ Unsupported signature method: {sha_name}")
            abort(401)
    except Exception as e:
        log(f"❌ Malformed signature header: {signature} | Error: {e}")
        abort(401)

    computed_hash = hmac.new(GITHUB_SECRET, msg=request.data, digestmod=hashlib.sha256).hexdigest()
    log(f"🔐 Received signature: {signature_hash}")
    log(f"🔐 Computed hash:     {computed_hash}")

    if not hmac.compare_digest(computed_hash, signature_hash):
        log("❌ Signature mismatch!")
        abort(401)

    log("✅ Signature valid. Pulling latest code...")
    os.system("cd /home/kade/StonewallNexus && git pull >> /tmp/github_webhook.log 2>&1")
    os.system("touch /var/www/kade_pythonanywhere_com_wsgi.py")

    log("✅ Deployment complete.")
    return "OK", 200