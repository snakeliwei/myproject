# elasticdump.sh
#!/usr/bin/env bash
# encoding: utf-8
# Author: lyndon
# dependence: elasticdump [npm i -g elasticdump]

set -ex
SRC="10.25.0.231:9201"
DEST="10.25.0.231:9202"
for index in \
    categories \
    herbs \
    organizations \
    products \
    subbranches \
; do \
    elasticdump --input=http://${SRC}/${index} --output=http://${DEST}/${index} --type=analyzer; \
    elasticdump --input=http://${SRC}/${index} --output=http://${DEST}/${index} --type=mapping; \
    elasticdump --input=http://${SRC}/${index} --output=http://${DEST}/${index} --type=data; \
done;