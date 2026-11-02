## Try the skills without installing

To try this library, load it from a local clone for a single Claude Code session. The skills are available only in that session, and nothing is installed permanently. This works because the library is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.

1. Clone the repository:

   ```sh
   git clone <repository-url> /path/to/clone
   ```

2. Start Claude Code with `--plugin-dir` pointing at the clone:

   ```sh
   claude --plugin-dir /path/to/clone
   ```

3. Ask Claude Code to do a task that matches a skill's description, then watch for a Skill tool call. Skills load on their own when a task matches, so the call confirms that the library is working.

Each skill keeps its reference files in its own `references/` directory. If the clone is outside your project, an agent may not be able to read those files unless you also pass the same path to `--add-dir`:

```sh
claude --plugin-dir /path/to/clone --add-dir /path/to/clone
```
