#!/usr/bin/env bash

rm inventory/host.ini
touch inventory/host.ini

rm .env
touch .env

. ./unimelb-COMP90024-2022-grp-35-openrc.sh; ansible-playbook --ask-become-pass deploy_instance.yaml