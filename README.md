# moregrowth.co: MoreGrowth Digital Solutions website

Static, bilingual site (Arabic at `/`, English at `/en/`). No build step, no CMS, no server: any static host serves it, with free HTTPS.

## Files
- `index.html`: Arabic (RTL, default)
- `en/index.html`: English
- `assets/`: stylesheet, `main.js` (scroll reveals, neural-network canvas, AI console demo, logo marquee), logo, favicon, social share image (`og.png`)
- `assets/clients/`: client logos (PNG, 160px tall, transparent). Add a file here and to the `CLIENTS` list in the generator to show a new logo
- `CNAME`: custom domain for GitHub Pages (`moregrowth.co`)
- `robots.txt`, `sitemap.xml`

## Deploy on GitHub Pages (free SSL)
1. Push this folder to a GitHub repository (e.g. `moregrowth-site`), default branch `main`.
2. Repository **Settings → Pages → Build and deployment**: Source = *Deploy from a branch*, Branch = `main` / `(root)`.
3. Custom domain: `moregrowth.co` (already set by the `CNAME` file).
4. At the domain's DNS provider, change **only** the web records:

| Type | Name | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | `<github-username>.github.io` |

   Delete any old A/AAAA records for `@` and `www`. **Do not touch MX, SPF/DKIM (TXT) records**, or `info@moregrowth.co` email will stop working.
5. Wait for DNS (minutes to a few hours), then tick **Enforce HTTPS** in Settings → Pages. GitHub issues and renews the Let's Encrypt certificate automatically.

## Editing content
Text lives directly in the two HTML files. Keep both languages in sync when changing a section.
