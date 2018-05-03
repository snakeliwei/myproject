# elasticdump.sh
#!/usr/bin/env bash
# encoding: utf-8
# Author: lyndon
# dependence: elasticdump [npm i -g elasticdump]

SRC=""
DEST=""
INDEXS="\
        index1 \
        index2 \
        "
for index in INDEXS
; do \
    elasticdump \
    --input=http://${SRC}/${index} \
    --output=http://${DEST}/${index} \
    --type=analyzer ;\ 
    elasticdump \
    --input=http://${SRC}/${index} \
    --output=http://${DEST}/${index} \
    --type=mapping ;\
    elasticdump \
    --input=http://${SRC}/${index} \
    --output=http://${DEST}/${index} \
    --type=data ;\
done; 



