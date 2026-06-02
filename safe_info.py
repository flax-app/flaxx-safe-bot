def get_info(user, me, os, version, branch, uptime, ram_usage, ping):
    return f"""
🤖 {me}

🟢 Status: Online

🌐 OS   : {os}
📦 Ver  : {version} ({branch})

⏱ Up   : {uptime}
🧠 RAM  : {ram_usage}
📡 Ping : {ping}ms

⚙️ CPU  : Safe Mode
"""
