# Planted defects in the retest fixture

The `tidy` skill is synthetic and built only to test `skill-review`. Don't show this file to a reviewer.

| ID | Defect | Rule that should catch it |
|---|---|---|
| D1 | The description claims code and repositories, so it loads on ordinary code work | 3 |
| D2 | "Never give a command from memory" while no command cites a source | 7 |
| D3 | Rule 2 says always ask before deleting; the reference deletes empty directories without asking | 7 |
| D4 | Says `mv -n` overwrites existing files; it refuses to overwrite | 8 |
| D5 | Says `ls -S` sorts by date; it sorts by size | 8 |
| D6 | "At most two moves at a time" can be obeyed with two moves of whole directories | 6 |
| D7 | "Tidiness is a habit that rewards patience." says nothing to do or check | 10 |
| D8 | Project claims Linux and macOS; `stat -c` is GNU only, and the demo tried Linux only | 4, 8 |
