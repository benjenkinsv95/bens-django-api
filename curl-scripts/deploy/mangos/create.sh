#!/bin/bash

# How to run this script:
# TOKEN=REPLACE_TOKEN_HERE NAME=Irwin COLOR=Red RIPE=True sh curl-scripts/deploy/mangos/create.sh

curl "https://bens-django-api.herokuapp.com/mangos/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "mango": {
      "name": "'"${NAME}"'",
      "color": "'"${COLOR}"'",
      "ripe": "'"${RIPE}"'"
    }
  }'

echo
