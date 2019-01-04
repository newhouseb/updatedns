import boto3
import socket
import sys
import dns.resolver

# Resolve the public IP via DNS
resolver = dns.resolver.Resolver()
resolver.nameservers=[socket.gethostbyname('resolver1.opendns.com')]
current_ip = None
for rdata in resolver.query('myip.opendns.com', 'A'):
    current_ip = rdata.to_text().strip()
if current_ip is None:
    logging.error("Unable to find an IP address from OpenDNS")
    sys.exit(-1)

# Find the hosted zone
record_to_update = sys.argv[1]
zone_to_update = '.'.join(record_to_update.split('.')[-2:])
conn = boto3.Session().client('route53')
zone = conn.list_hosted_zones_by_name(DNSName=zone_to_update)['HostedZones'][0]['Id']

# Check to see if it has the right IP
changed = True
try:
    existing = conn.list_resource_record_sets(HostedZoneId=zone, StartRecordName=record_to_update)['ResourceRecordSets'][0]['ResourceRecords'][0]['Value']
    if existing == current_ip:
        print("IP has not changed")
        changed = False
except:
    pass

# If not, update it
if changed:
    print("IP has changed, updating")
    conn.change_resource_record_sets(HostedZoneId=zone, ChangeBatch={
        'Changes': [{'Action': 'UPSERT',
            'ResourceRecordSet': {
                'Name': record_to_update,
                'ResourceRecords': [{
                    'Value': current_ip
                    }],
                'Type': 'A',
                'TTL': 60}}]
            })

