#!/bin/sh
CONF_DIR=/custom-config

docker run --rm -v ${WORK_DIR}:${WORK_DIR} -w ${WORK_DIR} -v /var/run/docker.sock:/var/run/docker.sock \
        --env WORK_DIR=${WORK_DIR} --env PROFILE=${PROFILE} --security-opt label:disable \
        --env CONF_DIR=${CONF_DIR} ${COMPOSE_IMAGE} \
        -f "${WORK_DIR}/TAF/utils/scripts/docker/docker-compose.yml" restart $*

# Waiting for edgex-kong cache released
if [ "$SECURITY_SERVICE_NEEDED" = "true" ]; then
  sleep 2
fi
