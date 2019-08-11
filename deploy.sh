#!/bin/bash

aws lambda update-function-code \
  --function-name coinwatch-python-5min \
  --zip-file fileb://handler.zip
