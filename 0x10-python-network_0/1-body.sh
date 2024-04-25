#!/bin/bash
# Takes a URL, sends  GET request to the URL, and displays body of the response
curl -Lsf "$1"
