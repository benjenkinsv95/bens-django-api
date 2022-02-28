#!/bin/bash

# TOKEN=REPLACE_TOKEN_HERE ID=REPLACE_ID_HERE NAME=Alphonso COLOR=Orange RIPE=False sh curl-scripts/deploy/mangos/update.sh

curl "https://bens-django-api.herokuapp.com/mangos/${ID}/" \
  --include \
  --request PATCH \
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
