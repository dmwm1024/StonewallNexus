
from app.github import github_bp

import os
import hmac
import hashlib
from flask import request, abort

LOGFILE = "/tmp/github_webhook.log"
REPO_PATH = "/home/kade/StonewallNexus"
WSGI_FILE = "/var/www/kade_pythonanywhere_com_wsgi.py"
GITHUB_SECRET = os.environ.get("GITHUB_SECRET", "").encode()

def log(message):
    with open(LOGFILE, "a") as f:
        f.write(message + "\n")

@github_bp.route('/github-webhook', methods=['POST'])
def github_webhook():
    log("🔔 Webhook hit!")

    # Get signature from GitHub headers
    signature = request.headers.get("X-Hub-Signature-256")
    if not signature:
        log("❌ No signature header found")
        abort(401)

    try:
        sha_name, signature_hash = signature.split("=")
        if sha_name != "sha256":
            log(f"❌ Unsupported signature method: {sha_name}")
            abort(401)
    except ValueError as e:
        log(f"❌ Invalid signature format: {signature} | Error: {e}")
        abort(401)

    # Compute our own hash
    computed_hash = hmac.new(GITHUB_SECRET, msg=request.data, digestmod=hashlib.sha256).hexdigest()

    if not hmac.compare_digest(computed_hash, signature_hash):
        log(f"❌ Signature mismatch!\nExpected: {computed_hash}\nReceived: {signature_hash}")
        abort(401)

    log("✅ Signature verified. Pulling latest changes...")

    # Pull from GitHub
    git_output = os.popen(f"cd {REPO_PATH} && git pull").read()
    log(git_output)

    # Reload app
    os.system(f"touch {WSGI_FILE}")
    log("🔁 App reloaded.")

    return "Webhook processed", 200
