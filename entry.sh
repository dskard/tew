#!/usr/bin/env bash

set -e

#set -x

function shutdown () {
    echo "Received SIGINT or SIGTERM. Shutting down $DAEMON"

    # Set TERM
    kill -SIGTERM "${PID}"

    # Wait for exit
    wait "${PID}"

    # All done.
    echo "Done."
}

echo "Running $@"

# setup signal trapping
# shutdown if we get the following signals
trap shutdown SIGINT SIGTERM

# run the command
$@ &

# Track the command through its PID
PID="$!"

# wait for the command to complete
wait "${PID}" && exit $?
