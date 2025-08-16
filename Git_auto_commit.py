# auto_utils.py
import os
import subprocess
from pathlib import Path


def git_auto_commit(repo_path, commit_msg="Auto commit"):
    """Git自动提交脚本"""
    os.chdir(repo_path)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_msg])
    subprocess.run(["git", "push"])


if __name__ == "__main__":
    # 示例：自动提交当前项目
    project_path = Path(__file__).parent
    git_auto_commit(project_path)