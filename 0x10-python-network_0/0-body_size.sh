#!/bin/bash
curl -sI $1/echo | grep -oP '(?<=Content-Length: )[0-9]+'
