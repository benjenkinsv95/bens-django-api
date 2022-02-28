#!/bin/bash

# TOKEN=REPLACE_TOKEN_HERE sh curl-scripts/deploy/mangos/index.sh

curl "https://bens-django-api.herokuapp.com/mangos/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
