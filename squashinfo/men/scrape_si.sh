#!/bin/bash

for line in `cat fetch_these`;
  do
  savename=`echo $line | cut -d'/' -f3`
  curl -s -o html/$savename http://www.squashinfo.com"$line"
  echo "done $savename"
done
