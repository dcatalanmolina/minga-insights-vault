<!-- Banner auto-swaps with the viewer's GitHub light/dark theme -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/minga-banner-dark.png">
    <img src=".github/assets/minga-banner-light.png" alt="minga-insights-vault" width="640">
  </picture>
</p>

<p align="center">
  <em>Communal knowledge, gathered.</em>
</p>

<!-- Optional: badges. Replace OWNER/REPO and delete any you don't want. -->
<p align="center">
  <a href="https://github.com/dcatalanmolina/minga-insights-vault/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/dcatalanmolina/minga-insights-vault"></a>
  <a href="https://github.com/dcatalanmolina/minga-insights-vault/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/dcatalanmolina/minga-insights-vault"></a>
  <a href="https://github.com/dcatalanmolina/minga-insights-vault/issues"><img alt="Issues" src="https://img.shields.io/github/issues/dcatalanmolina/minga-insights-vault"></a>
</p>

---

`minga-insights-vault` is an open-source vault to gather insights, influence decisions, and track strategy, powered by collaboration-first agents.

- Use Obsidian and [Quadro](https://github.com/chrisgrieser/obsidian-quadro) (community plugin) to discover, write, and organize user and customer insights. Quadro allows you to code text from interviews, meeting notes, and other sources. 
- The folder structure and conventions are harness-agnostic; you can use Claude Code, Codex, etc. The repo follows the [Agent Skill standard](https://agentskills.io/home) for portable skills and agents. 

Get started by firing up your harness and giving it this instruction:

```
Review the AGENTS.md file and invoke minga-host to help me get started
```

## How to analyze and organize insights

- Use the `Projects` folder to share an overview of the projects associated with data, insights, and decisions.
- Use the `Data` folder to add new documents with interview transcripts, meeting notes, and other sources of qualitative data. Within each document, highlight paragraphs or sentences to code into different themes using Quadro's side panel. 
- Everything you code will be automatically organized in the `Codes` folder. Quadro does this for you. You shouldn't edit documents in the `Codes` folder.
- Create a new document under `Analysis` to take notes. Your notes will depend on the question you are answering and the themes and categories you notice inside `Codes`.
- Synthesize your analyses by writing insights in a format that makes product development easier. 
- Create a new canvas in `Global Notes` to organize insights and to facilitate discussion with others.

Learn more about the conventions to name files [here](docs/conventions.md).

**New here?** Follow the [Getting Started](docs/getting-started.md) walkthrough for a step-by-step example.

## About the name

A *minga* is a tradition of communal labor and reciprocity from rural southern Chile — neighbors coming together to raise a house or bring in a harvest, work shared and given back in turn. This project is a vault built the same way: knowledge gathered by many hands.

## Contributing

Contributions are welcome — in the spirit of the minga. See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.
- If you have an idea for a collaboration-first agent, but don't know how to implement it, add a new issue describing its goals, principles, and skills. We can build it together.

- If you find bugs or gaps in the file system or agent layer, add a new issue describing what doesn't work for you, why, and in what situation. The more gaps people report, the easier it will be to build something that scales.

- If you want to contribute as an active developer building new features, let me know!

## License

MIT