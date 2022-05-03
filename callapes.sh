#!/bin/bash

: '
node nodelean.js 300 400
sleep 5
node nodelean.js 400 500
sleep 5
node nodelean.js 500 600'

allThreads=()

input="mayc-105-2-c.txt"
while IFS= read -r line
do
  echo "$line"
  node nodelean.js $line >> the_results.txt
  sleep 0.1
done < "$input"


: '
for t in ${allThreads[@]}; do
  echo "$t"
  node nodelean.js $t
  sleep 0.2
done'