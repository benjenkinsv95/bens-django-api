# How to run this script:
# EMAIL=b@b.com PASSWORD=bbbbb sh curl-scripts/local/auth/sign-up.sh

curl "http://localhost:8000/skill-tracker/sign-up/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
    "credentials": {
      "email": "'"${EMAIL}"'",
      "password": "'"${PASSWORD}"'",
      "passwordConfirmation": "'"${PASSWORD}"'"
    }
  }'

echo
