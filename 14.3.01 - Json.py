import json

data = json.loads(input())  # Преобразуем строку JSON обратно в словарь

print('🚨 Обнаружена угроза! Немедленно прими меры!' if data['status'] == 'danger'
      else '✅ Передача безопасна. Продолжай наблюдение.')