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
    signature = request.headers.get('X-Hub-Signature-256', '')
    sha_name, signature = signature.split('=')
    mac = hmac.new(GITHUB_SECRET, msg=request.data, digestmod=hashlib.sha256)

    if not hmac.compare_digest(mac.hexdigest(), signature):
        abort(403)

    subprocess.Popen(["/home/kade/StonewallNexus/deploy_hook.py"])
    return 'Success', 200
