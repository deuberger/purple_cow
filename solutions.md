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

# Install Dependencies

    sudo apt install docker.io docker-compose

# Run

    sudo docker-compose up

# Other commands

    # Restart
    sudo docker-compose down
    sudo docker-compose up

    # Much more serious restart and show logs
    sudo ./docker-compose-restart-clean.sh

Note that there may be spurious logs during startup since docker compose doesn't validate the DB is ready to accept connections before starting app.

# Examples

    curl -H "Content-Type: application/json" -X POST -d '[{"name": "item1"},{"name": "item2"}]' http://localhost:3000/item/
    curl http://localhost:3000/item/
    curl -X DELETE http://localhost:3000/item/
    curl http://localhost:3000/item/<id>
    curl -H "Content-Type: application/json" -X PUT -d '{"name": "Freddy"}' http://localhost:3000/item/<id>
    curl -X DELETE http://localhost:3000/item/<id>

# FUTURE

 * Make the port easily configurable and documented
 * Upgrade to a production worthy web server
 * Refactor tests to improve code reuse
 * Update tests to use docker postgresql container (same setup as prod)
 * Return number of items deleted for DELETE /item
 * Clean up / improve environemnt and config settings
 * Config has setups that aren't being used
 * Add automated integration tests
 * The docker-compose-restart-clean.sh script could be better (or maybe there's
   a better solution altogether)
