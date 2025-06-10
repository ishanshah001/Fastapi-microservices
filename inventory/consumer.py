from main import redis_inv, Product
import time
from redis_om import get_redis_connection, HashModel
from dotenv import load_dotenv
import os

load_dotenv()

key = 'order_completed'
group = 'inventory-group'

redis_payment = get_redis_connection(
    host= os.getenv("REDDIS_ENDPOINT_PAYMENT"),
    port=12172,
    password= os.getenv("REDDIS_PASSWORD_PAYMENT"),
    decode_responses=True
)

try:
    redis_payment.xgroup_create(key, group, mkstream=True)
except:
    print('Group already exists!')

while True:
    try:
        results = redis_payment.xreadgroup(group, key, {key: '>'}, None)
        if results != []:
            for result in results:
                obj = result[1][0][1]
                try:
                    product = Product.get(obj['product_id'])
                    product.quantity = product.quantity - int(obj['quantity'])
                    product.save()
                except:
                    redis_payment.xadd('refund_order', obj, '*')

    except Exception as e:
        print(str(e))
    time.sleep(1)
