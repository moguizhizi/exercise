# -*- coding: utf-8 -*-
import lmdb

# 如果train文件夹下没有data.mbd或lock.mdb文件，则会生成一个空的，如果有，不会覆盖
# map_size定义最大储存容量，单位是kb，以下定义1TB容量
env = lmdb.open("./train"，map_size = 1099511627776)
env.close()
