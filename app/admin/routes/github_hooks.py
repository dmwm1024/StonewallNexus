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
    print("🔔 Webhook route hit!")

    signature = request.headers.get("X-Hub-Signature-256")
    if signature is None:
        print("❌ No signature received.")
        abort(401, "Missing signature")

    try:
        sha_name, signature_hash = signature.split("=")
        if sha_name != "sha256":
            print(f"❌ Unsupported signature method: {sha_name}")
            abort(401, "Unsupported signature")
    except Exception as e:
        print(f"❌ Malformed signature: {signature} | Error: {e}")
        abort(401, "Malformed signature")

    computed_hash = hmac.new(GITHUB_SECRET, msg=request.data, digestmod=hashlib.sha256).hexdigest()

    print("🔐 Received signature:", signature_hash)
    print("🔐 Computed hash:     ", computed_hash)

    if not hmac.compare_digest(computed_hash, signature_hash):
        print("❌ Signature mismatch!")
        abort(401, "Invalid signature")

    print("✅ Signature validated. Pulling code...")
    os.system("cd /home/kade/StonewallNexus && git pull")
    os.system("touch /var/www/kade_pythonanywhere_com_wsgi.py")

    return "Webhook received", 200