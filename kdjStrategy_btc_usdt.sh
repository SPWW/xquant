#!/bin/bash

source ~/.profile
base_dir=$(cd `dirname $0`; pwd)

python3.6 $base_dir/main.py strategy/kdj KDJStrategy '{"symbol":"btc_usdt", "digits":{"btc":8,"usdt":2}, "exchange":"binance", "sec": 600, "limit":20, "id": "1"}'
