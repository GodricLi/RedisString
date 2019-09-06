# _*_ coding=utf-8 _*_


import redis
from Interview.Redis.RedisPool.redis_pool import pool

"""RedisString（字符串）
string 是 redis 最基本的类型，你可以理解成与 Memcached 一模一样的类型，一个 key 对应一个 value。
string 类型是二进制安全的。意思是 redis 的 string 可以包含任何数据。比如jpg图片或者序列化的对象。
string 类型是 Redis 最基本的数据类型，string 类型的值最大能存储 512MB。"""
# 连接池
coon = redis.Redis(connection_pool=pool)
# 设置值 set(key,value)
coon.set('a', 1)
# 获取值 get(key)
print(coon.get('a'))

# 设置多个{k:v,k:v}
coon.mset({'b': 2, 'c': 3})
print(coon.mget('b', 'c'))

# incr对key的值做加法操作，并返回新的值
print(coon.incr('b', 1))

# decr对key的值做减法操作，并返回新的值
print(coon.decr('b', 3))

# incrby/decrby(key,int) 加/减指定值
coon.incrby('b', 5)
print(coon.get('b'))

# append(key, value)给key追加指定值
coon.append('b', 'a')
print(coon.get('b'))
