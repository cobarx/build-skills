## Try the library without installing it

You can try these skills for a single Claude Code session, and nothing is installed permanently. The repository is itself a plugin directory (its manifest is at `.claude-plugin/plugin.json`), so Claude Code can load it directly from a clone.

To start a session with the skills available, follow these steps:

1. Clone the repository:

   ```sh
   git clone <repository-url> /path/to/library
   ```

2. Start Claude Code with `--plugin-dir` pointing at the clone:

   ```sh
   claude --plugin-dir /path/to/library
   ```

3. Check that the skills load by asking for a task that matches a skill's description, then watching for a Skill tool call. You don't need to invoke a skill by name, because skills load on their own when the task matches their description.

Each skill keeps its reference files in its own `references/` directory. If the clone is outside your project, an agent may not be able to read those files until you also pass the same path to `--add-dir`:

```sh
claude --plugin-dir /path/to/library --add-dir /path/to/library
```

The skills stop being available when the session ends. To use them again, start Claude Code with the same flags.
