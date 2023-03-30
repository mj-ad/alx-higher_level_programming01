#!/bin/bash
# sends a delete requezt to an url and gets the body of the response
curl -sX DELETE $1 -L
