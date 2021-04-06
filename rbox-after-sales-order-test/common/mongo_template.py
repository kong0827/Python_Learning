import logging

from pymongo import MongoClient

from common import constant
from common.application_config import ApplicationConfig


class MongoTemplate:
    def __init__(self, col=None):
        self.config = ApplicationConfig()
        self.uri = self.config.get_value('DB', 'as.mongodb.uri')
        self.db = self.config.get_value('DB', 'as.mongodb.db')
        self.collection = col if col is None else self.config.get_value('DB', 'as.mongodb.collection')
        self.conn = None

    # 获取mongo数据库链接
    def get_cursor(self):
        self.conn = MongoClient(self.uri)
        return self.conn

    # 关闭链接
    def close(self):
        self.conn.close()

    # 获取操作文档
    def get_collection(self):
        conn = self.get_cursor()
        db = conn[self.db]
        collection = db[self.collection]
        return collection

    # 查询单个文档
    def get_one(self, filter={}, fields=None):
        res = None
        try:
            collection = self.get_collection()
            res = collection.find_one(filter) if fields is None else collection.find_one(filter, fields)
        except Exception as e:
            logging.error("查询失败,{}", e)
        finally:
            self.close()
        return res

    # 查询所有文档
    def get_all(self, filter={}, fields=None):
        res = None
        try:
            collection = self.get_collection()
            res = collection.find(filter) if fields is None else collection.find(filter, fields)
        except Exception as e:
            logging.error("查询失败,{}", e)
        finally:
            self.close()
        return res

    # 分页查询
    def get_page_query(self, filter={}, fields=None, page=0, size=10, sort=None):
        res = None
        try:
            skip = size * page
            collection = self.get_collection()
            res = collection.find(filter).skip(skip) if fields is None else (
                collection.find(filter, fields).limit(
                    size).skip(skip)
                if sort is None else collection.find(filter, fields).limit(
                    size).skip(skip).sort(sort)
            )
        except Exception as e:
            logging.error("查询失败,{}", e)
        finally:
            self.close()
        return res

    # 插入一个文档
    def insert_one(self, document):
        x = None
        try:
            collection = self.get_collection()
            x = collection.insert_one(document)
        except Exception as e:
            logging.error("插入失败,{}", e)
        finally:
            self.close()
        return x

    # 插入多个文档
    def insert_many(self, documents):
        xs = None
        try:
            collection = self.get_collection()
            xs = collection.insert_many(documents)
        except Exception as e:
            logging.error("插入失败,{}", e)
        finally:
            self.close()
        return xs

    # 更新数据
    def update_one(self, filter, update):
        x = None
        try:
            collection = self.get_collection()
            x = collection.update_one(filter, update)
        except Exception as e:
            logging.error("插入失败,{}", e)
        finally:
            self.close()
        return x

    def update(self, filter, update):
        x = None
        try:
            collection = self.get_collection()
            x = collection.find_and_modify(query, update)
        except Exception as e:
            logging.error("插入失败,{}", e)
        finally:
            self.close()
        return x

    # 删除文档
    def delete_one(self, filter):
        collection = self.get_collection()
        collection.delete_one(filter)


if __name__ == '__main__':
    n = MongoTemplate(constant.mongo_collection)
    for item in n.get_all(fields={'id'}):
        print(item)

    print('-----------')
    for item in n.get_page_query(fields={'id'}):
        print(item)

    print('------插入一个数据--------')
    x = n.insert_one({'aftersalesNo': 'test', 'orderStatus': 1})

    print('------修改一个数据--------')
    query = {'aftersalesNo': 'test'}
    update = {"$set": {"aftersalesNo": "new-test"}}
    n.update_one(query, update)

    print('------删除一个数据--------')
    query = {'aftersalesNo': 'new-test'}
    n.delete_one(query)
