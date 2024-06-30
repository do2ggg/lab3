import requests
import json

def search_repositories(query):
  """
  Функція пошуку репозиторіїв GitHub за заданим ключовим словом.

  Args:
    query: Ключове слово для пошуку.

  Returns:
    Список репозиторіїв у форматі JSON.
  """
  url = f"https://api.github.com/search/repositories?q={query}"
  headers = {"Authorization": f"token YOUR_TOKEN"}  # Додайте свій токен доступу до GitHub
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    return json.loads(response.text)["items"]
  else:
    print(f"Помилка при пошуку репозиторіїв: {response.status_code}")
    return []

def print_repositories(repositories):
  """
  Функція друкує список знайдених репозиторіїв.

  Args:
    repositories: Список репозиторіїв у форматі JSON.
  """
  for repository in repositories:
    print(f"* {repository['name']}: {repository['description']}")

def main():
  """
  Головна функція програми.
  """
  query = input("Введіть ключове слово для пошуку: ")
  repositories = search_repositories(query)
  print(f"Знайдено {len(repositories)} репозиторіїв:")
  print_repositories(repositories)

if __name__ == "__main__":
  main()

