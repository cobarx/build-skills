## Try the library without installing it

To try the skills for a single Claude Code session, clone the repository and point `--plugin-dir` at the clone. Nothing is installed permanently.

Replace `<repository-url>` and `/path/to/clone` with your own values:

1. Clone the repository:

   ```sh
   git clone <repository-url> /path/to/clone
   ```

2. Start Claude Code from your project, with the clone as the plugin directory:

   ```sh
   claude --plugin-dir /path/to/clone
   ```

3. Ask for a task that matches a skill's description, and watch for a Skill tool call. Skills load on their own when the task matches, so you don't need to invoke them by name.

If the clone is outside your project, an agent may not be able to read the files in each skill's `references/` directory. To give it access, pass the same path to `--add-dir`:

```sh
claude --plugin-dir /path/to/clone --add-dir /path/to/clone
```

`--plugin-dir` accepts the clone because the repository is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.
