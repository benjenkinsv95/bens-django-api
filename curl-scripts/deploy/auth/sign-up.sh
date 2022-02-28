# How to run this script:
# EMAIL=b@b.com PASSWORD=bbbbb sh curl-scripts/deploy/auth/sign-up.sh

curl "https://bens-django-api.herokuapp.com/sign-up/" \
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
