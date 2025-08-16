# auto_commit.py 改进版
import subprocess
import os

import time
MIN_INTERVAL = 300  # 5分钟
last_commit_time = 0  # 实际应从文件或变量中读取

if time.time() - last_commit_time < MIN_INTERVAL:
    print(f"⏳ 距离上次提交不足{MIN_INTERVAL}秒，跳过")
    exit(0)


def git_auto_commit():
    repo_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_path)

    try:
        # 拉取更新
        pull = subprocess.run(["git", "pull", "origin", "main"],
                              capture_output=True, text=True)
        print("拉取结果:\n", pull.stdout)

        # 提交变更
        commit = subprocess.run(["git", "commit", "-am", "Auto commit by script"],
                                capture_output=True, text=True)
        print("提交结果:\n", commit.stdout)

        # 推送
        push = subprocess.run(["git", "push", "origin", "main"],
                              capture_output=True, text=True)
        print("推送结果:\n", push.stdout)

        print("✅ 所有操作成功完成！")
    except subprocess.CalledProcessError as e:
        print("❌ 执行失败:\n", e.stderr)

# 检查是否有待提交的修改
status = subprocess.run(["git", "status", "--porcelain"],
                       capture_output=True, text=True)
if not status.stdout.strip():
    print("⚠️ 没有检测到文件变更，跳过提交")
    exit(0)

if __name__ == "__main__":
    git_auto_commit()

