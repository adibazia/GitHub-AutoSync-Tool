import subprocess
import random

def get_modified_files():
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
    if not status:
        return []
    
    files = []
    for line in status.split('\n'):
        parts = line.strip().split()
        if len(parts) >= 2:
            files.append(parts[-1])
    return files

def generate_smart_default(file_name):
    # Professional conventional commit messages based on file type
    if file_name.endswith('.py'):
        templates = [
            f"refactor: optimize workflow execution in {file_name}",
            f"feat: extend core logic within {file_name}",
            f"fix: resolve edge case handling in {file_name}",
            f"style: refine code structure and imports in {file_name}"
        ]
    elif file_name.endswith('.md'):
        templates = [
            f"docs: update project description in {file_name}",
            f"docs: refine setup instructions in {file_name}"
        ]
    else:
        templates = [
            f"chore: update {file_name} configurations",
            f"refactor: clean up workspace structure in {file_name}"
        ]
    
    return random.choice(templates)

def run():
    # 1. Stage changes
    subprocess.run(["git", "add", "."])
    
    # 2. Detect changes
    changed_files = get_modified_files()
    if not changed_files:
        print("No changes detected to push.")
        return

    # 3. User input with professional dynamic fallback
    primary_file = changed_files[0]
    default_msg = generate_smart_default(primary_file)
    
    print(f"Detected file: {primary_file}")
    user_msg = input("Enter commit message (Press Enter for auto-generate): ").strip()
    
    commit_msg = user_msg if user_msg else default_msg

    # 4. Commit and push
    print(f"\nCommitting: '{commit_msg}'")
    subprocess.run(["git", "commit", "-m", commit_msg])
    
    print("Pushing to GitHub...")
    push = subprocess.run(["git", "push"], capture_output=True, text=True)

    if push.returncode == 0:
        print("Done! Changes synced successfully.")
    else:
        print("Push failed:", push.stderr)

if __name__ == "__main__":
    run()