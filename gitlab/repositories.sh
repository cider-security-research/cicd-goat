#!/bin/sh
export GIT_ASKPASS=/setup/askpass.py
export GIT_USERNAME=root
export GIT_PASSWORD=ciderland5#
cd repositories

cd pygryphon && git push -u origin main && cd ..
cd awesome-app && git push -u origin main && cd ..
cd nest-of-gold && git push -u origin main && cd ..

cd ..