import subprocess
import datetime

print("--- Git Auto-Sync Tool Setup ---")

# 1. Staging Files (git add .)
print("Files add ho rahi hain...")
subprocess.run(["git", "add", "."])

# 2. Professional Commit Message Input
user_msg = input("\nAapne kya changes kiye hain? (Commit message likhein): ")

# Agar input khaali choda toh smart default message banega
if not user_msg.strip():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_message = f"docs: update project files {now}"
else:
    commit_message = user_msg.strip()

print(f"\nCommitting with message: '{commit_message}'")
subprocess.run(["git", "commit", "-m", commit_message])

# 3. Final Status Check
result = subprocess.run(["git", "status"], capture_output=True, text=True)
print("\nFinal Status:")
print(result.stdout)