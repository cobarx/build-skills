## Try it without installing

To try the skills in Claude Code, clone the repository and start a session with `--plugin-dir` pointing at the clone:

```sh
git clone <repository-url> /path/to/clone
claude --plugin-dir /path/to/clone
```

The skills are available for that session only. This works because the repository is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.

Skills load on their own when a task matches their description. To check that they're working, ask for a task that one of them covers and watch for a Skill tool call.

Each skill keeps its reference files in its `references/` directory. If the clone is outside your project, an agent may need `--add-dir` with the same path to read them:

```sh
claude --plugin-dir /path/to/clone --add-dir /path/to/clone
```
