import threading
from redis import ConnectionPool
import redis

pool = ConnectionPool(host='localhost', port=6379, db=0)

def worker():
    r = redis.Redis(connection_pool=pool)
    r.incr('counter')

threads = [threading.Thread(target=worker) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(r.get('counter').decode('utf-8'))