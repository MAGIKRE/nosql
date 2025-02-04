from redis import ConnectionPool
import redis

pool = ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

r.set('key', 'value')
print(r.get('key').decode('utf-8'))