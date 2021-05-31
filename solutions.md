# Assumptions

 * Assumed items id is determined by the app and not setable by the user

# TODO
    sudo apt install postgresql libpq-dev
    sudo -u postgres createdb test_db
    sudo -u postgres createdb purple_cow
    sudo -u postgres createuser azureuser

    pg_hba.conf
    host    all             all             127.0.0.1/32            trust

    pip3 install - requirements.txt

    DATABASE_URL="postgresql://localhost/test_db" python3 -m flask db upgrade
    python3 -m unittest

    source .env
    python3 run.py

# FUTURE

 * Refactor tests to improve code reuse
 * Return number of items deleted for DELETE /item
