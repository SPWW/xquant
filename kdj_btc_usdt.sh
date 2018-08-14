#!/bin/bash

source ~/.profile
base_dir=$(cd `dirname $0`; pwd)
echo $1
python3.6 $base_dir/main.py strategy/kdj KDJStrategy \
    '{"symbol":"btc_usdt", "sec": 600}' \
    '{
        "limit":{"value":100, "mode":0},
        "exchange":"binance",
        "commission_rate": 0.001,
        "digits":{"btc":6,"usdt":2},
        "select":"real",
        "real":{"instance_id": "x11"},
        "backtest":{"start_time":"2018-06-30 00:00:00", "end_time":"2018-08-11 00:00:00"}}' \
    $1
