# Caddy routing change for public read-only demo (not applied)

Current `/etc/caddy/Caddyfile`:

```caddy
prozesspilot.duckdns.org {
    basicauth * {
        demo [REDACTED_PASSWORD_HASH]
    }
    @api path /api/* /health /docs* /openapi.json
    handle @api {
        reverse_proxy 127.0.0.1:8000
    }
    handle {
        root * /opt/prozesspilot/frontend/dist
        try_files {path} /index.html
        file_server
    }
}
```

Proposed Caddyfile:

```caddy
prozesspilot.duckdns.org {
    route {
        @public path / /demo /demo/* /public/* /assets/* /favicon.ico
        handle @public {
            @snapshot path /public/*
            handle @snapshot {
                reverse_proxy 127.0.0.1:8000
            }
            handle {
                root * /opt/prozesspilot/frontend/dist
                try_files {path} /index.html
                file_server
            }
        }

        basicauth * {
            demo [REDACTED_PASSWORD_HASH]
        }

        @protected path /api/* /health /docs* /openapi.json /app* /runs/* /eval /eval/*
        handle @protected {
            reverse_proxy 127.0.0.1:8000
        }

        handle {
            root * /opt/prozesspilot/frontend/dist
            try_files {path} /index.html
            file_server
        }
    }
}
```

Notes:
- `/`, `/demo`, static assets, and `/public/*` are public.
- `/public/demo-snapshot` returns the reviewed static snapshot only.
- `/api/*`, `/health`, docs, `/app*`, `/runs/*`, and `/eval*` remain behind basic auth.
- No secrets, provider keys, or credentials are added to frontend code or public assets.

Apply after review (not in this task):

```sh
sudo cp /etc/caddy/Caddyfile /etc/caddy/Caddyfile.pre-public-demo
# write proposed file to /etc/caddy/Caddyfile
sudo caddy validate --config /etc/caddy/Caddyfile
sudo systemctl reload caddy
```

Rollback:

```sh
sudo cp /etc/caddy/Caddyfile.pre-public-demo /etc/caddy/Caddyfile
sudo caddy validate --config /etc/caddy/Caddyfile
sudo systemctl reload caddy
```
