
    sudo apt install postgresql libpq-dev
    sudo -u postgres createdb test_db
    sudo -u postgres createdb purple_cow
    sudo -u postgres createuser azureuser

    source .env
    
    pg_hba.conf
    host    all             all             127.0.0.1/32            trust
