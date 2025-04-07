#!/bin/bash

PRODUCT_ID=${1:-1}

echo "Updating product with ID: $PRODUCT_ID"

status=$(curl -L -X PUT http://localhost:8000/product/$PRODUCT_ID \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Updated Product",
        "price": 29.99,
        "description": "Updated description"
      }' \
  -o /dev/null \
  -s \
  -w "%{http_code}")

if [[ $status == 200 ]]; then
  echo "Product updated successfully (HTTP Code: $status)"
else
  echo "Error while updating product (HTTP Code: $status)"
  exit 1
fi
