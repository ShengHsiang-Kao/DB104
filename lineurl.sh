#!/bin/bash

curl -s "localhost:54089/api/tunnels" | awk -F',' '{print $3}' | awk -F'"' '{print $4}' | awk -F'//' '{print $2}'
