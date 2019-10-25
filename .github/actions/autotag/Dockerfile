FROM python:alpine

RUN apk update && apk add bash git curl ca-certificates jq

COPY entrypoint.sh /entrypoint.sh
COPY get_new_tag.py /get_new_tag.py

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
