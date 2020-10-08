#!/usr/bin/env python
# encoding: utf-8
import multiprocessing
import math
import os
import sys

POOL_ADDRESS = sys.argv[1]
WALLET_ADDRESS = sys.argv[2]
WORKER = sys.argv[3]

if len(sys.argv) > 4:
    CPU_USAGE = int(sys.argv[4])
else:
    CPU_USAGE = 75

if CPU_USAGE == 100:
    os.system("xmrig -o {} -u {}.{} -p x --donate-level=0 --tls --randomx-1gb-pages --keepalive  --cpu-priority=0 --cpu-no-yield".format(POOL_ADDRESS, WALLET_ADDRESS, WORKER))
else:
    if multiprocessing.cpu_count() == 1:
        os.system("cpulimit -l {} -- xmrig -o {} -u {}.{} -p x --donate-level=0 --tls --randomx-1gb-pages --keepalive  --cpu-priority=0 --cpu-no-yield".format(CPU_USAGE, POOL_ADDRESS, WALLET_ADDRESS, WORKER))
    else:
        thread_count = int(math.floor(multiprocessing.cpu_count() * 0.01 * CPU_USAGE))
        os.system("xmrig -o {} -u {}.{} -p x --donate-level=0 --tls --threads={} --randomx-1gb-pages --keepalive  --cpu-priority=0 --cpu-no-yield".format(POOL_ADDRESS, WALLET_ADDRESS, WORKER, thread_count))
