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
    signature = request.headers.get("X-Hub-Signature-256")
    if signature is None:
        abort(401, "No signature provided.")

    try:
        sha_name, signature = signature.split('=')
        if sha_name != 'sha256':
            abort(401, "Unsupported signature method.")
    except Exception:
        abort(401, "Invalid signature format.")

    mac = hmac.new(GITHUB_SECRET, msg=request.data, digestmod=hashlib.sha256)
    
    print("GitHub signature:", signature)
    print("Computed hash:", mac.hexdigest())

    return "Success", 200