#!/bin/bash
awk '{print $3}' out_*.txt | sort | uniq -c | sort -r | head -n 160
