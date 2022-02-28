# How to run this script:
# TOKEN=REPLACE_TOKEN_HERE OLDPW=bbbbb NEWPW=ccccc sh curl-scripts/local/auth/change-pw.sh

curl "http://localhost:8000/change-pw/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "passwords": {
      "old": "'"${OLDPW}"'",
      "new": "'"${NEWPW}"'"
    }
  }'

echo
