#!/bin/bash

COUNTER_FILE="./counter.txt"


NUM=$(cat "$COUNTER_FILE")

python3 async_run.py ./CreateDataset.ipynb waste
rm waste.ipynb

OUTPUT_NB="experiment${NUM}"

echo $OUTPUT_NB

python3 async_run.py ./TrainModel.ipynb "$OUTPUT_NB"

NUM=$((NUM + 1))

echo "$NUM" > "$COUNTER_FILE"