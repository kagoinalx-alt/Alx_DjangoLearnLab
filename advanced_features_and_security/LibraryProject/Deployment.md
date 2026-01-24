## HTTPS Deployment Configuration

HTTPS is enforced at the web server level using Nginx.

### HTTP to HTTPS Redirect
```nginx
server {
    listen 80;
    server_name example.com;

    return 301 htttps://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/ssl/certs/example.crt;
    ssl_certificate_key /etc/ssl/private/example.key;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-For $remote_addr;
    }
}
