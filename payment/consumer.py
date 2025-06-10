from main import redis_payment, Order
import time
from redis_om import get_redis_connection, HashModel
from dotenv import load_dotenv
import os

load_dotenv()

key = 'refund_order'
group = 'payment-group'

try:
    redis_payment.xgroup_create(key, group, mkstream=True)
except:
    print('Group already exists!')

while True:
    try:
        results = redis_payment.xreadgroup(group, key, {key: '>'}, None)

        if results != []:
            print(results)
            for result in results:
                obj = result[1][0][1]
                order = Order.get(obj['pk'])
                order.status = 'refunded'
                order.save()

    except Exception as e:
        print(str(e))
    time.sleep(1)
