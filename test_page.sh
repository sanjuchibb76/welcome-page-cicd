#!/bin/sh
set -e
grep -q "Welcome" index.html
echo "PASS: welcome page test"
