#/bin/sh
docker run -d \
    --name purple_cow-postgres \
    -e POSTGRES_PASSWORD=veryverysecret \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v /tmp/pgdata:/var/lib/postgresql/data \
    postgres
docker run -it --rm  \
    -e APP_SETTINGS=production \
    -e SECRET="kadkfjlakjflkajgljhargfoJHEGO;JAEGFJKVAL;KJFL;KJAL;DKJFL;KJ" \
    -e DATABASE_URL="postgresql://localhost/purple_cow" \
    -p 5000:5000 \
    --name purple_cow purple_cow
