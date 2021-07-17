import redis

redis=redis.Redis('localhost',decode_responses=True)

all_keys=redis.keys()

print(all_keys)           # to find allll the values in our localhost

# print(redis.type('counters'))
# print(redis.hgetall('counters'))    # to get all the values from one 

# redis.set('a',1)        # to se value of a 1
# print(redis.get('a'))    # to get the value of a

# redis.set('s',"hey there")         # to set value of s
# print(redis.get('s'))             # to get value of s
# redis.set('s',"hey theere how are you?")
# print(redis.get('s'))             # to get value of s

# redis.delete('a')         # to delete a
# redis.delete('s')         # to delete s
# redis.delete('dict')