import pytest
from pymongo import MongoClient


# single mongo
# c = MongoClient(host="mongo-1", port=28010) # okay
# c = MongoClient('mongodb://admin:123456@mongo-1:28010,mongo-2:28010/?replicaSet=rsname')

# mongo cluster

def getCollection():
    c = MongoClient(
        'mongodb://rbox:DfbfkcVBUa@192.168.1.177:3701,192.168.1.176:3701,192.168.1.178:3701/rbox-after-sales-dev')
    db = c["rbox-after-sales-dev"]
    collection = db["after_sales_order_r1"]
    return collection


def test_find_one():
    """
    查询一条记录
    :return:
    """
    collection = getCollection()
    res = collection.find_one()
    print(res)
    assert len(res) is not None


def test_find_all():
    """
    查询集合中所有的数据
    :return:
    """
    collection = getCollection()
    size = 0
    arr = []
    for x in collection.find():
        arr.append(x)
        size = size + 1
    print(len(arr))
    assert size > 0
