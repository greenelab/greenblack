
[Complete Rxivist dataset of scraped bioRxiv data (Version 2019-01-20)](https://doi.org/10.5281/zenodo.2544998)


ZENODO_ID=2544998
wget https://zenodo.org/record/$ZENODO_ID/files/rxivist.backup


```sh
# Run docker container for rxivist database
docker run \
  --name=rxivist \
  --publish=65500:5432 \
  postgres:11.1

# Restore rxdb database into postgres container
docker exec --interactive rxivist \
  pg_restore --clean --create --no-acl --no-owner --username postgres --dbname postgres < rxivist.backup
```






 psql -h localhost -U postgres
 docker exec --interactive --tty rxivist bash


select * FROM prod.article_publications LIMIT 5;