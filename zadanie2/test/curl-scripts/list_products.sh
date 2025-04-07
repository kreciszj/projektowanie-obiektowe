#!/bin/bash

echo "Listing products..."

status=$(curl -L -X GET http://localhost:8000/product/ \
  -o /dev/null \
  -s \
  -w "%{http_code}")

if [[ $status == 200 ]]; then
  echo "Product list fetched successfully (HTTP Code: $status)"
else
  echo "Error while fetching product list (HTTP Code: $status)"
  exit 1
fi
