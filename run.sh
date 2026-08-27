# NOTE: when using this script, it can execute any application in the "app" folder
# the name of the wanted application must be passed as the first argument
# NOTE: if the application wants to be started as setup (so by executing the "setup" function in the designated application)
# then the second argument must be "setup"
# NOTE: any other argument will be passed or converted based on what it is or what the application needs to run

#!/bin/bash
# ─────────────────────────────────────────────────────────────
#  Cardinal – run.sh
#
#  Usage:
#    ./run.sh <app> run         → start in DEV mode
#    ./run.sh <app> stop        → stop the app and DB containers
#    ./run.sh <app> reset       → destroys the DB and rebuilds it
#    ./run.sh <app> setup       → setup DB and executes the "setup" function
#    ./run.sh <app> build       → creates an image for PROD baked mode
#    ./run.sh <app> deploy      → starts the app in PROD (standalone)
# ─────────────────────────────────────────────────────────────

# NOTE: remove this
# echo "this script is currently being developed, please do not use this script"
# exit 0

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
COMPOSE_DEV="$SCRIPT_DIR/docker-compose.yml"
COMPOSE_PROD="$SCRIPT_DIR/docker-compose.prod.yml"

VALID_APPS=($(ls -d "$SCRIPT_DIR/app"/*/  2>/dev/null | xargs -n1 basename))

if [ ${#VALID_APPS[@]} -eq 0 ]; then
  echo "No app found in $SCRIPT_DIR/app/"
  exit 1
fi

if [ $# -lt 2 ]; then
  echo "Usage: ./run.sh <app> <command>"
  echo "-- Available apps: ${VALID_APPS[*]}"
  exit 1
fi

if [[ ! " ${VALID_APPS[@]} " =~ " $1 " ]]; then
  echo "Invalid app selected: $1"
  echo "-- Available apps: ${VALID_APPS[*]}"
  exit 1
fi

APP_NAME="$1"
COMMAND="$2"
CONTAINER="cardinal_${APP_NAME}"
DB_SERVICE="db_${APP_NAME}"

if [ "$COMMAND" == "reset" ]; then
  docker compose -f "$COMPOSE_DEV" stop "$APP_NAME" "$DB_SERVICE"
  echo "- Resetting DB volumes for app $APP_NAME..."
  docker compose -f "$COMPOSE_DEV" down -v "$APP_NAME" "$DB_SERVICE"
  docker compose -f "$COMPOSE_DEV" up -d "$APP_NAME" "$DB_SERVICE"
  echo "-- Reset completed."
  exit 0
fi

if [ "$COMMAND" == "stop" ]; then
  docker compose -f "$COMPOSE_DEV" stop "$APP_NAME" "$DB_SERVICE"
  exit 0
fi

if [ "$COMMAND" == "build" ]; then
  echo "Building production image for $APP_NAME..."
  docker build \
    --build-arg APP_NAME="$APP_NAME" \
    -t "kemonobat4/cardinal-${APP_NAME}:latest" \
    "$SCRIPT_DIR"
  echo "-- Image ready: kemonobat4/cardinal-${APP_NAME}:latest"
  echo "- Saving Tar..."
  docker save "kemonobat4/cardinal-${APP_NAME}:latest" \
    -o "$SCRIPT_DIR/cardinal-${APP_NAME}.tar"
  echo "-- Tar saved as cardinal-${APP_NAME}.tar"
  exit 0
fi

if [ "$COMMAND" == "deploy" ]; then
  echo "- Production deployment of $APP_NAME..."
  docker compose -f "$COMPOSE_PROD" up -d "$APP_NAME" "$DB_SERVICE"
  echo "-- $APP_NAME deployed."
  exit 0
fi

echo "Starting in DEV mode: $APP_NAME + $DB_SERVICE"
docker compose -f "$COMPOSE_DEV" up -d "$APP_NAME" "$DB_SERVICE"

echo "- Waiting for $CONTAINER to start..."
until docker ps --filter "name=^${CONTAINER}$" --filter "status=running" \
      --format '{{.Names}}' | grep -q "^${CONTAINER}$"; do
  sleep 1
done

if [ "$COMMAND" == "setup" ]; then
  docker compose -f "$COMPOSE_DEV" stop "$APP_NAME" "$DB_SERVICE"
  docker compose -f "$COMPOSE_DEV" exec "$APP_NAME" \
    pip install -r --no-cache-dir requirements.txt
fi

# print compose dev name
echo "- Starting $APP_NAME..."
echo "what is $COMPOSE_DEV"

docker compose -f "$COMPOSE_DEV" exec -it "$APP_NAME" \
  python run.py "$APP_NAME" "$COMMAND"


# TODO: commands to handle
# [CREATE NEW APP] ./run.sh cardinal new application <application_name>