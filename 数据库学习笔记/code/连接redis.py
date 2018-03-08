from redis import *


if __name__ == '__main__':
    sr = StrictRedis(decode_responses=True)

    sr.set('avalon','123456')
    sr.get('avalon')