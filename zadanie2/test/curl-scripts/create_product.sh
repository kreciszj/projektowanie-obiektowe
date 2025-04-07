#!/bin/bash

echo "Creating product..."

status=$(curl -X POST http://localhost:8000/product/create \
  -H "Content-Type: application/json" \
  -d '{
        "id": 1,
        "name": "Example Product",
        "price": 19.99,
        "description": "Some product"
      }' \
  -o /dev/null \
  -s \
  -w "%{http_code}" \
  -L )


if [[ $status == 200 ]]; then
  echo "Product created successfully (HTTP Code: $status)"
else
  echo "Error while creating product (HTTP Code: $status)"
  exit 1
fi
