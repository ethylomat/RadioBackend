#!/usr/bin/env bash
ssh -o StrictHostKeyChecking=no root@ethylomat.de << 'ENDSSH'
 cd /backend
 docker login -u $REGISTRY_USER -p $CI_BUILD_TOKEN $CI_REGISTRY
 docker pull registry.gitlab.com/awesomeradio/backend:latest
 docker-compose up -d
ENDSSH
