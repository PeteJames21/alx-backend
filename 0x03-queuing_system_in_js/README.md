# 0x03-queuing_system_in_js

# Files

## dump.rdb

Contains a dump file of a new database containing only the key-value pair `Holberton="School"

## 0-redis_client.js

Using Babel and ES6, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:

- It should log to the console the message `Redis client connected` to the server when the connection to Redis works correctly
- It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work
- Connect to Redis using the `redis` package from npm

## 1-redis_op.js

In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).

Add two functions:

    setNewSchool:
        It accepts two arguments schoolName, and value.
        It should set in Redis the value for the key schoolName
    displaySchoolValue:
        It accepts one argument schoolName.
        It should log to the console the value for the key passed as argument

At the end of the file, call:

    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');

## 4-redis_advanced_op.js

Use `HSET` to store a hash value and `HGETALL` to retrieve the object stored.
