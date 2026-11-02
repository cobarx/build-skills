## Try the skills without installing them

You can try this library for a single Claude Code session by cloning it and pointing Claude Code at the clone. The skills are available only in that session, and nothing is installed permanently.

To start a session with the skills and confirm they work:

1. Clone the repository:

   ```sh
   git clone <repository-url> ~/skill-library
   ```

2. From your project, start Claude Code with `--plugin-dir` pointing at the clone:

   ```sh
   claude --plugin-dir ~/skill-library
   ```

   If the clone is outside your project, an agent may not be able to read the files in each skill's `references/` directory. To give it access, pass the same path to `--add-dir`:

   ```sh
   claude --plugin-dir ~/skill-library --add-dir ~/skill-library
   ```

3. Ask Claude Code to do a task that matches a skill's description, then watch for a Skill tool call. You don't need to invoke the skill yourself, because skills load on their own when a task matches their description.

The `--plugin-dir` flag works here because the repository is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.
