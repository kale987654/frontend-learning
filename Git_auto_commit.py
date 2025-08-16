# auto_commit.py
import subprocess
import os


def git_auto_commit():
    repo_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_path)

    # 先拉取更新避免冲突
    subprocess.run(["git", "pull", "origin", "main"], check=True)

    # 添加修改（排除venv）
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Auto commit by script"])
    subprocess.run(["git", "push", "origin", "main"])


if __name__ == "__main__":
    git_auto_commit()