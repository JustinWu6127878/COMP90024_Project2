#!/usr/bin/env bash

ansible-playbook -i inventory/host.ini -u ubuntu  setup_couchdb.yaml