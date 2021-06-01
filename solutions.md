# Overview

This is the purple cow prototype application.

# Assumptions

 * Assumed items id is determined by the app and not setable by the user

# Testing

    sudo apt install postgresql libpq-dev
    sudo -u postgres createdb test_db
    sudo -u postgres createuser azureuser

    pg_hba.conf
    host    all             all             127.0.0.1/32            trust

    sudo systemctl restart postgresql

    pip3 install - requirements.txt

    source .env
    python3 -m flask db upgrade
    python3 -m unittest

# Running

    # Install dependencies
    sudo apt install docker.io docker-compose

    # Stop postgres to avoid conflicts if you have it running locally

    # Start
    sudo docker-compose up

    # Restart
    sudo docker-compose down
    sudo docker-compose up

    # Much more serious restart
    sudo ./docker-compose-restart-clean.sh

Note that there may be spurious logs during startup since docker compose doesn't validate the DB is ready to accept connections before starting app.

# Examples

    curl http://localhost:5000/item/

# FUTURE

 * Make the port easily configurable and documented
 * Upgrade to a production worthy web server
 * Refactor tests to improve code reuse
 * Update tests to use docker postgresql container (same setup as prod)
 * Return number of items deleted for DELETE /item
 * Clean up / improve environemnt and config settings
 * Config has setups that aren't being used
 * Add more exmple curl lines above
 * Add automated integration tests
 * The docker-compose-restart-clean.sh script could be better (or maybe there's
   a better solution altogether)
