#!/bin/sh
# Builds the repo every parallel-work case runs in: a git repo on main with a typo'd README and
# a few scripts, and a dev server serving it from this checkout on port 8000.
set -eu
git init -q -b main .
mkdir -p scripts
printf '# demo\n\nWe recieve input on stdin.\n' > README.md
printf '#!/bin/sh\necho "hello"\n' > scripts/greet.sh
printf '#!/bin/sh\nwc -l\n' > scripts/summarize.sh
printf '#!/bin/sh\nexec python3 -m http.server 8000 --bind 127.0.0.1\n' > dev.sh
chmod +x scripts/*.sh dev.sh
printf '.claude/worktrees/\n' > .gitignore
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m "Initial commit"
(setsid ./dev.sh >/dev/null 2>&1 &) || true
