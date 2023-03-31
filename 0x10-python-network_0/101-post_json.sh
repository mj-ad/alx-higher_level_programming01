#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument and displays the response body
curl -sX POST $1 -H "Content-type: application/json" -d @$2
