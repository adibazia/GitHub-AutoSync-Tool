import subprocess
import datetime

print("--- Professional GitHub Auto-Sync Tool ---")

# 1. Stage all files
print("[1/3] Staging files...")
subprocess.run(["git", "add", "."])

# 2. Get professional commit message
user_msg = input("\nEnter commit message (Press Enter for default): ").strip()

if not user_msg:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_message = f"chore: routine code updates {now}"
else:
    commit_message = user_msg

# 3. Commit changes
print(f"\n[2/3] Committing with message: '{commit_message}'")
subprocess.run(["git", "commit", "-m", commit_message])

# 4. Push to GitHub
print("\n[3/3] Syncing with GitHub...")
push_result = subprocess.run(["git", "push"], capture_output=True, text=True)

if push_result.returncode == 0:
    print("\n✅ Auto-Sync Successful! All changes pushed to GitHub.")
else:
    print("\n❌ Push failed. Output:")
    print(push_result.stderr)