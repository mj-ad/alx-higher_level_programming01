#!/bin/bash
# using curl to get the body size of a url
curl -sI $1 | grep -oP '(?<=Content-Length: )[0-9]+'
