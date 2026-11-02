## Try the skills without installing them

To try the skills for a single Claude Code session, clone the repository and point `--plugin-dir` at the clone. Nothing is installed permanently.

1. Clone the repository:

   ```sh
   git clone <repository-url> /path/to/clone
   ```

2. Start Claude Code with the clone as a plugin directory:

   ```sh
   claude --plugin-dir /path/to/clone
   ```

   If the clone is outside your project, add `--add-dir` with the same path:

   ```sh
   claude --plugin-dir /path/to/clone --add-dir /path/to/clone
   ```

3. Ask Claude Code to do a task that matches a skill's description, and watch for a Skill tool call, which shows that the skill loaded.

Skills load when a task matches their description, so you don't need to invoke them by name.

An agent may need `--add-dir` to read each skill's `references/` directory when the clone is outside your project.

`--plugin-dir` works because the repository is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.
