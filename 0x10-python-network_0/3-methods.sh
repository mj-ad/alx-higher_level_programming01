#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -siX OPTIONS $1 |grep Allow: | cut -c 8- ; echo ""
