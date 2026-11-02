## Try the skills for one session

You can try this library in Claude Code without installing it permanently. When you load it from a local clone with `--plugin-dir`, the skills are available for that session only.

To load the library and check that it works, follow these steps:

1. Clone the repository, replacing `<repository-url>` and `/path/to/clone` with your own values:

   ```sh
   git clone <repository-url> /path/to/clone
   ```

2. From your project directory, start Claude Code with `--plugin-dir` pointing at the clone:

   ```sh
   claude --plugin-dir /path/to/clone
   ```

3. Ask Claude Code to do a task that matches one of the skills, then watch for a Skill tool call. Skills load on their own when a task matches their description, so you don't need to invoke them by name.

Each skill keeps its reference files in its own `references/` directory. If the clone is outside your project, an agent may not be able to read those files unless you also pass the same path to `--add-dir`:

```sh
claude --plugin-dir /path/to/clone --add-dir /path/to/clone
```

`--plugin-dir` works here because the library is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.
