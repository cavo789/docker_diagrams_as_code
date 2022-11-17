#!/usr/bin/env bash

cat php_team.py | docker run -i --rm -v $(pwd)/images:/out gtramontina/diagrams:0.22.0

cat premise.py | docker run -i --rm -v $(pwd)/images:/out gtramontina/diagrams:0.22.0
