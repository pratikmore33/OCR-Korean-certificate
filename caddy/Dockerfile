FROM caddy/caddy:2.4.6-alpine

WORKDIR /app

COPY start.sh /app/start.sh

COPY Caddyfile /etc/caddy/Caddyfile

CMD ["sh", "/app/start.sh"]