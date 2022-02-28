#!/bin/bash

# TOKEN=REPLACE_TOKEN_HERE ID=REPLACE_ID_HERE sh curl-scripts/local/practices/delete.sh

curl "http://localhost:8000/skill-tracker/practices/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
