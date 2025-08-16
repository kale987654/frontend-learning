# 检查 Python
Write-Host "=== Python 检查 ===" -ForegroundColor Cyan
$pyPath = (Get-Command python -ErrorAction SilentlyContinue).Source
if ($pyPath) {
    Write-Host "[√] 找到 Python: $pyPath" -ForegroundColor Green
    python --version
} else {
    Write-Host "[×] 未找到 Python" -ForegroundColor Red
}

# 检查 PyCharm 可用的解释器
Write-Host "`n=== 可用解释器 ===" -ForegroundColor Cyan
Get-ChildItem -Path @("C:\Python*", "${env:ProgramFiles}\Python*") -Filter "python.exe" -Recurse | ForEach-Object {
    Write-Host $_.FullName
}

# 建议
if (-not $pyPath) {
    Write-Host "`n请从 https://www.python.org/downloads/ 安装 Python 并勾选 'Add to PATH'" -ForegroundColor Yellow
}