# Unpaywall datasets

Learn more about Unpaywall at https://unpaywall.org.

Download Unpaywall data:

```
# https://github.com/greenelab/greenblack/issues/1
URL=https://s3-us-west-2.amazonaws.com/unpaywall-data-snapshots/unpaywall_snapshot_2018-09-24T232615.jsonl.gz

# Download subset
curl --silent $URL | gunzip | head --lines=100 > unpaywall_snapshot_2018-09-24T232615-subset.jsonl

# Download entirety
wget $URL
```
