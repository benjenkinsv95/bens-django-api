#!/bin/bash

# TOKEN=REPLACE_TOKEN_HERE sh curl-scripts/local/practices/index.sh

curl "http://localhost:8000/skill-tracker/practices/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
