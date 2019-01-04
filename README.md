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

*To run every 30 minutes*
```
crontab -e
```
Then add
```
*/30 * * * * docker run -e AWS_ACCESS_KEY_ID='[access key]' -e AWS_SECRET_ACCESS_KEY='[secret access key]' -e DOMAIN='[domain, i.e. server.bennewhouse.com]' updatedns
```




