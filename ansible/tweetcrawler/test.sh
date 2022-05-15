#!/usr/bin/env bash
rm front_end/.env
touch front_end/.env

ansible-playbook test.yaml