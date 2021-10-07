import os
import sys
import redis

path1 = os.path.abspath(__file__)
path2 = os.path.dirname(path1)
path3 = os.path.join(path2,"data","uuuu.xml")
print(path1)
print(path2)
print(path3)

#
# redis = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
# redis.set('name', 'junxi')  # key是"foo" value是"bar" 将键值对存入redis缓存
# print(redis['name'])
# print(redis.get('name'))  # 取出键name对应的值
# print(type(redis.get('name')))


from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='localhost', port=6379)
redis1 = StrictRedis(connection_pool=pool)
redis = redis.Redis(connection_pool=pool)
# redis.flushall()  # 清空Redis
# redis.setex('name', value='liaogx', time=2)  # 设置新值，过期时间为3s
# redis.mset(k1 = 'v1', k2 = 'v2', k3 = 'v3')  # 批量设置新值
# print(redis.mget('k1', 'k2', 'k3', 'k4'))  # 批量获取新值
# print(redis.getset('name', 'liaogaoxiang'))  # 设置新值并获取原来的值

print(redis.get('name'))  # 设置新值并获取原来的值

import sys
print(sys.path)








