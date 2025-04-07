#!/bin/bash

PRODUCT_ID=${1:-1}

echo "Deleting product with ID: $PRODUCT_ID"

status=$(curl -L -X DELETE http://localhost:8000/product/$PRODUCT_ID \
  -w "%{http_code}" -s -o /dev/null)

if [[ $status == 200 ]]; then
  echo "Product deleted successfully (HTTP Code: $status)"
else
  echo "Error while deleting product (HTTP Code: $status)"
  exit 1
fi
