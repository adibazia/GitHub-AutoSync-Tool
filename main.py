import subprocess
import random

def run():
    # 1. Stage changes
    subprocess.run(["git", "add", "."])
    
    # 2. Check for staged files
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
    if not status:
        print("No changes detected to push.")
        return

    # Real human-like developer commit messages
    clean_messages = [
        "Update main script logic",
        "Improve workflow handling",
        "Refactor core sync functionality",
        "Minor fixes and code updates",
        "Update project scripts",
        "Clean up internal logic"
    ]
    
    # 3. User input with natural default fallback
    user_msg = input("Enter commit message (Press Enter for auto-generate): ").strip()
    commit_msg = user_msg if user_msg else random.choice(clean_messages)

    # 4. Commit and push
    print(f"\nCommitting: '{commit_msg}'")
    subprocess.run(["git", "commit", "-m", commit_msg])
    
    print("Syncing with GitHub...")
    push = subprocess.run(["git", "push"], capture_output=True, text=True)

    if push.returncode == 0:
        print("Done! Changes synced successfully.")
    else:
        print("Push failed:", push.stderr)

if __name__ == "__main__":
    run()