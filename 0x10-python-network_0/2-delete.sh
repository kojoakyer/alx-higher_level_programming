#!/bin/bash
# Script that sends  DELETE request to the URL passed as the first argument and displays the body of the response
curl -sX DELETE "$1"
