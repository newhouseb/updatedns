# updatedns
Dynamic DNS Updater that uses Route53 and OpenDNS to resolve a public IP

# Usage (with Docker)

*To build*
```
docker build -t updatedns .
```

*To run*
```
docker run -e AWS_ACCESS_KEY_ID='[access key]' -e AWS_SECRET_ACCESS_KEY='[secret access key]' -e DOMAIN='[domain, i.e. server.bennewhouse.com]' updatedns
```

*To run every 5 minutes*
```
crontab -e
```
Then add
```
*/5 * * * * docker run -e AWS_ACCESS_KEY_ID='[access key]' -e AWS_SECRET_ACCESS_KEY='[secret access key]' -e DOMAIN='[domain, i.e. server.bennewhouse.com]' updatedns
```

# Other handy commands for certbot:

```
sudo apt-get install python3-certbot-dns-route53 python3-certbot-nginx
sudo certbot --dns-route53 -i nginx -d "*.server.bennewhouse.com" -d server.bennewhouse.com --server https://acme-v02.api.letsencrypt.org/directory
sudo certbot renew --dry-run # Put this in a crontab most likely
```
