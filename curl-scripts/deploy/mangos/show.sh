#!/bin/bash

# TOKEN=REPLACE_TOKEN_HERE ID=REPLACE_ID_HERE sh curl-scripts/deploy/mangos/show.sh

curl "https://bens-django-api.herokuapp.com/mangos/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
