from redis import Redis


class RedisClient:
    """
    写入数据到redis
    """

    def __init__(self, host, port, db, password):
        self.redis = Redis(host=host, port=port, db=db, password=password)

    def write_data(self, key, value):
        """"""
        """
        写入数据到redis
        :param data: 数据
        :return:
        """
        self.redis.sadd(key, value)

    def write_data_list(self, key, values):
        """"""
        """
        写入数据到redis
        :param data: 数据
        :return:
        """
        for value in values:
            self.redis.sadd(key, value)

    # 获取所有数据
    def get_list_all(self, key):
        """"""
        """
        获取所有数据
        :return:
        """
        data = [v.decode("utf-8") for v in self.redis.smembers(key)]
        return data


class FakeData:
    """
    生成数据
    """

    def __init__(self, env, ips):
        self.env = env
        self.ips = ips


dev_ips = ["192.168.200.1", "192.168.200.2", "192.168.200.3", "192.168.200.4"]
prod_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]
stg_ips = ["192.168.100.1", "192.168.100.2", "192.168.100.3", "192.168.100.4"]

redis_client = RedisClient("", 6379, 1, password="")
# redis_client.write_data_list("dev", dev_ips)
# redis_client.write_data_list("prod", prod_ips)
redis_client.write_data_list("stg", stg_ips)
data = redis_client.get_list_all("stg")
print(data)
for value in data:
    print(value)
