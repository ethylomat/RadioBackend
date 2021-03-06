#!/usr/bin/env bash
ssh -o StrictHostKeyChecking=no root@ethylomat.de << 'ENDSSH'
 cd /backend
 docker login -u $REGISTRY_USER -p $CI_BUILD_TOKEN $CI_REGISTRY
 git pull
 docker-compose up -d --build
ENDSSH
