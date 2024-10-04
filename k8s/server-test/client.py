import requests

try:
    response = requests.get('http://localhost:5000')
    response.raise_for_status()  # проверка на наличие ошибок HTTP
    print(response.text)
except requests.exceptions.ConnectionError:
    print("Не удается подключиться к серверу. Проверьте, запущен ли сервер.")
except requests.exceptions.HTTPError as err:
    print(f"HTTP ошибка: {err}")
except requests.exceptions.RequestException as e:
    print(f"Ошибка: {e}")
