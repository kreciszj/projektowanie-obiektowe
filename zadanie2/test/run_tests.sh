#!/bin/bash

echo "Running all curl-based tests..."

TEST_DIR="./curl-scripts/"

# create_product.sh
echo "Executing test: ${TEST_DIR}create_product.sh"
bash "${TEST_DIR}create_product.sh"
if [[ $? -ne 0 ]]; then
  echo "Create product test failed"
  exit 1
fi
echo -e "\n-----------------------------------------\n"

# update_product.sh
echo "Executing test: ${TEST_DIR}update_product.sh"
bash "${TEST_DIR}update_product.sh"
if [[ $? -ne 0 ]]; then
  echo "Update product test failed"
  exit 1
fi
echo -e "\n-----------------------------------------\n"

# delete_product.sh
echo "Executing test: ${TEST_DIR}delete_product.sh"
bash "${TEST_DIR}delete_product.sh"
if [[ $? -ne 0 ]]; then
  echo "Delete product test failed"
  exit 1
fi
echo -e "\n-----------------------------------------\n"

# list_products.sh
echo "Executing test: ${TEST_DIR}list_products.sh"
bash "${TEST_DIR}list_products.sh"
if [[ $? -ne 0 ]]; then
  echo "List products test failed"
  exit 1
fi
echo -e "\n-----------------------------------------\n"

echo "All tests executed."
