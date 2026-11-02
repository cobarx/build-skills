## Try the skills without installing them

To try these skills, clone the repository and point Claude Code at the clone with `--plugin-dir`. The skills are available for that session only, and nothing is installed permanently.

1. Clone the repository:

   ```sh
   git clone <repository-url> /path/to/clone
   ```

2. Start Claude Code from your project, using the path to the clone:

   ```sh
   claude --plugin-dir /path/to/clone
   ```

   This works because the repository is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.

3. Ask Claude Code to do a task that matches a skill's description, then watch for a Skill tool call. You don't need to invoke the skill yourself, because skills load on their own when a task matches their description.

Each skill keeps its reference files in its own `references/` directory. If the clone is outside your project, the agent may not be able to read those files until you pass the same path to `--add-dir`:

```sh
claude --plugin-dir /path/to/clone --add-dir /path/to/clone
```
