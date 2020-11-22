#https://pypi.org/project/redis/
#server https://github.com/MicrosoftArchive/redis/releases

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo'))
print(r.get('NA'))

