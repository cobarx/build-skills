## Try it without installing

You can try this library for a single Claude Code session, and nothing is installed permanently. To start a session with the skills available, clone the repository and point `--plugin-dir` at the clone:

```sh
git clone <repository-url> ~/skill-library
claude --plugin-dir ~/skill-library
```

The clone's root is the plugin directory, and its manifest is at `.claude-plugin/plugin.json`. To stop using the skills, start Claude Code without the flag.

### Check that the skills load

You don't need to invoke the skills by hand, because each one loads on its own when a task matches its description. To check that this is working, ask Claude Code to do a task that matches a skill's description, then watch for a Skill tool call.

### Give access to reference files

Each skill keeps its reference files in its own `references/` directory. If the clone is outside your project, an agent may not be able to read those files until you also pass the clone's path to `--add-dir`:

```sh
claude --plugin-dir ~/skill-library --add-dir ~/skill-library
```
