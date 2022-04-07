#!/bin/bash

CMD=$(basename "${0}")

if [ ${#} -ne 1 ]; then
  echo "usage: ${CMD} <previous-version-tag>"
  exit 1
fi

FROM=${1}

npm run changelog -- --from ${FROM} | grep -v "^>" > CHANGELOG.add.md \
  && cat CHANGELOG.add.md CHANGELOG.md > CHANGELOG.new.md.tmp \
  && (
    lines=$(cat CHANGELOG.new.md.tmp | wc -l)
    tail -n $(expr $lines - 1) CHANGELOG.new.md.tmp > CHANGELOG.new.md
  ) \
  && rm CHANGELOG.add.md CHANGELOG.new.md.tmp \
  && (
    echo "CHANGELOG.new.md was created and is ready for review"
    echo "Simply move CHANGELOG.new.md to CHANGELOG.md when you are done and commit the new changelog"
    echo "mv CHANGELOG.new.md CHANGELOG.md"
  )
