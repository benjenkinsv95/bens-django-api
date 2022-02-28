#!/bin/bash

# TOKEN=REPLACE_TOKEN_HERE ID=REPLACE_ID_HERE sh curl-scripts/deploy/mangos/delete.sh

curl "https://bens-django-api.herokuapp.com/mangos/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
