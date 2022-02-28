# How to run this script:
# TOKEN=REPLACE_TOKEN_HERE sh curl-scripts/local/auth/sign-out.sh

curl "http://localhost:8000/skill-tracker/sign-out/" \
  --include \
  --request DELETE \
  --header "X-CSRFToken: ${CSRF}" \
  --header "Authorization: Token ${TOKEN}" \

echo
