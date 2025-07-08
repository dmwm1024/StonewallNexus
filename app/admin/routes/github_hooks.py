# in routes/github_hooks.py
from flask import Blueprint, request, abort
import hmac
import hashlib
import subprocess
from app.admin import admin
import os

GITHUB_SECRET = os.environ.get("GITHUB_SECRET", 'FAIL').encode()

@admin.route('/github-webhook', methods=['POST'])
def github_webhook():
    # Step 1: Get signature from GitHub
    signature = request.headers.get("X-Hub-Signature-256")

    if signature is None:
        print("No signature received")
        abort(401, "Missing signature")

    try:
        sha_name, signature_hash = signature.split("=")
        if sha_name != "sha256":
            print("Unsupported signature method:", sha_name)
            abort(401, "Unsupported signature")
    except ValueError:
        print("Malformed signature:", signature)
        abort(401, "Malformed signature")

    # Step 2: Compute HMAC digest
    computed_hash = hmac.new(GITHUB_SECRET, msg=request.data, digestmod=hashlib.sha256).hexdigest()

    # Step 3: Debug output
    print("Received signature:", signature_hash)
    print("Computed hash: ", computed_hash)

    # Step 4: Validate signature
    if not hmac.compare_digest(computed_hash, signature_hash):
        print("Signature mismatch!")
        abort(401, "Invalid signature")

    # Step 5: Pull latest code
    print("Signature validated. Pulling latest code...")
    os.system("cd /home/kade/StonewallNexus && git pull")

    # Optional: reload app
    os.system("touch /var/www/kade_pythonanywhere_com_wsgi.py")

    print("Webhook processing complete.")
    return "Webhook received and processed", 200