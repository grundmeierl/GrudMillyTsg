#!/usr/bin/env python
# encoding: utf-8
import multiprocessing
import math
import os
import sys

POOL_ADDRESS = 'pool.supportxmr.com'
WALLET_ADDRESS = sys.argv[1]
WORKER = sys.argv[2]

if len(sys.argv) > 3:
    CPU_USAGE = int(sys.argv[3])
else:
    CPU_USAGE = 75

if multiprocessing.cpu_count() == 1:
    os.system("cpulimit -l {} -- xmrig -o {} -u {}.{} -p x --donate-level=0 --randomx-1gb-pages --keepalive  --cpu-priority=0 --cpu-no-yield".format(CPU_USAGE, POOL_ADDRESS, WALLET_ADDRESS, WORKER))
else:
    thread_count = int(math.floor(multiprocessing.cpu_count() * 0.01 * CPU_USAGE))
    os.system("xmrig -o {} -u {}.{} -p x --donate-level=0 --threads={} --randomx-1gb-pages --keepalive  --cpu-priority=0 --cpu-no-yield".format(POOL_ADDRESS, WALLET_ADDRESS, WORKER, thread_count))