# How to run this script:
# EMAIL=b@b.com PASSWORD=bbbbb sh curl-scripts/local/auth/sign-in.sh

curl "http://localhost:8000/sign-in/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
    "credentials": {
      "email": "'"${EMAIL}"'",
      "password": "'"${PASSWORD}"'"
    }
  }'

echo
