# How to run this script:
# TOKEN=REPLACE_TOKEN_HERE sh curl-scripts/deploy/auth/sign-out.sh

curl "https://bens-django-api.herokuapp.com/sign-out/" \
  --include \
  --request DELETE \
  --header "X-CSRFToken: ${CSRF}" \
  --header "Authorization: Token ${TOKEN}" \

echo
