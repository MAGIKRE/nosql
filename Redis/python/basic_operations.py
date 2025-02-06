r.set('username', 'JohnDoe')

r.setex('session_key', 3600, 'session_data')

print(r.get('username').decode('utf-8'))

r.hset('user:1', 'name', 'Alice')
r.hmset('user:1', {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'})
print(r.hgetall('user:1'))

r.lpush('fruits', 'apple', 'banana')
r.rpush('fruits', 'cherry', 'date')
print(r.lrange('fruits', 0, -1))

r.sadd('colors', 'red', 'green', 'blue')
print(r.smembers('colors'))

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('user:1:name', 'John Doe')
r.set('user:1:email', 'john.doe@example.com')

print(r.get('user:1:name').decode('utf-8'))
print(r.get('user:1:email').decode('utf-8'))


