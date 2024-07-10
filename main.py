import redis

r = redis.Redis(host='localhost', port=6379, db=0)

pubsub = r.pubsub()

pubsub.subscribe('mi_canal')

for mensaje in pubsub.listen():
    
    if mensaje['type'] == 'message':
        print(f"Mensaje recibido: {mensaje['data'].decode('utf-8')}")
