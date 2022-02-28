#!/bin/bash

# TOKEN=REPLACE_TOKEN_HERE ID=REPLACE_ID_HERE sh curl-scripts/local/mangos/show.sh

curl "http://localhost:8000/skill-tracker/mangos/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
