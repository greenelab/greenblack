# Rxivist downloads

Download data from [Complete Rxivist dataset of scraped bioRxiv data (Version 2019-01-20)](https://doi.org/10.5281/zenodo.2544998) and load it into a postgres database.
More information on Rxivist available at https://rxivist.org and https://doi.org/10.1101/515643.

```
# Download Zenodo datasets
ZENODO_ID=2544998
wget https://zenodo.org/record/$ZENODO_ID/files/figures.md --output-document=rxivist-figures.md
wget https://zenodo.org/record/$ZENODO_ID/files/rxivist.backup
```

```sh
# Run docker container for rxivist database
docker run \
  --name=rxivist \
  --publish=65500:5432 \
  postgres:11.1

# Restore rxdb database into postgres container
docker exec --interactive rxivist \
  pg_restore --clean --create --no-acl --no-owner --username postgres --dbname postgres < rxivist.backup

# To enter a shell inside the docker
docker exec --interactive --tty rxivist bash

# To enter a psql interactive session inside the docker shell
psql --host localhost --username postgres
```
