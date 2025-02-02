import os
import subprocess
import getpass
import requests
import json

# 🔹 Ввод данных пользователя
gitlab_url = "http://10.77.0.107/api/v4"
gitlab_group_id = "193"  # ID группы в GitLab, куда создаётся проект

gitlab_token = getpass.getpass("Введите ваш GitLab Token: ")
project_name = "{{ cookiecutter.project_name }}"

use_gitlab = input("🔗 Хотите связать проект с GitLab? (y/n): ").strip().lower()
if use_gitlab != "y":
    print("✅ Проект создан без интеграции с GitLab.")
    exit(0)
    
# 🔹 Проверяем введён ли токен
if not gitlab_token:
    print("❌ Ошибка: Не введён GitLab Token.")
    exit(1)

# 🔹 Создание репозитория в GitLab без README
headers = {"PRIVATE-TOKEN": gitlab_token, "Content-Type": "application/json"}
project_data = {
    "name": project_name,
    "path": project_name,
    "namespace_id": gitlab_group_id,
    "visibility": "private",
    "initialize_with_readme": False  # ❌ Убираем авто-инициализацию README.md
}

print(f"🚀 Создаём проект {project_name} в GitLab...")
response = requests.post(f"{gitlab_url}/projects", headers=headers, json=project_data)

if response.status_code == 201:
    project_info = response.json()
    project_git_url = project_info["ssh_url_to_repo"]
    print(f"✅ Репозиторий создан: {project_git_url}")
else:
    print(f"❌ Ошибка при создании проекта: {response.json()}")
    exit(1)

# 🔹 Инициализация локального Git-репозитория
print("📂 Инициализируем локальный репозиторий...")
subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "remote", "add", "origin", project_git_url], check=True)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
subprocess.run(["git", "branch", "-M", "main"], check=True)
subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

print("🚀 Репозиторий загружен в GitLab!")

