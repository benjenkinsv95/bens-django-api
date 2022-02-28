#!/bin/bash

# TOKEN=REPLACE_TOKEN_HERE sh curl-scripts/local/mangos/index.sh

curl "http://localhost:8000/mangos/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
