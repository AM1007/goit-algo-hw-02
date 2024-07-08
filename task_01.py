import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()

# Функція generate_request(request_id): створення заявки та додавання її до черги
def generate_request(request_id):
  request = {"id": request_id, "data": f"Data for request {request_id}"}
  request_queue.put(request)
  print(f"Generated request {request_id}")

# Функція process_request(): видалення заявки з черги та оброблення її
def process_request():
  if not request_queue.empty():
    request = request_queue.get()
    print(f"Processing request {request['id']}: {request['data']}")
  else:
    print("Queue is empty. No requests to process")

def main():
  request_id = 1
  while True:
    # Імітація генерування нових заявок з випадковими затримками
    generate_request(request_id)
    request_id += 1

    # Імітація обробки заявок з випадковими затримками
    process_request()

    # Випадкова затримка між 1 і 3 секундами
    time.sleep(random.randint(1, 3))

    # Зупинка програми після 10 ітерацій для прикладу
    if request_id > 5:
      break

if __name__ == "__main__":
  main()