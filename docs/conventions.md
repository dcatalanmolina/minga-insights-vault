# Conventions

## File Names
This repo uses a specific naming pattern for markdown files. A prefix indicates the type of content: 
- `DAT-` for data (e.g., interview transcript, meeting notes, report summary)
- `CDE-` for codes representing themes or sub-themes in the data 
- `INS-` for insights
- `DCN-` for decisions

After the prefix, a sequential 4-digit ID differentiates unique, *atomic* pieces of content. For example, two different interviews can be saved as `DAT-0001` and `DAT-0002`.

This naming pattern enforces a *modular* structure across data, codes, insights, and decisions. Obsidian and its community plugins work best with folders that enforce a modular structure. Also, when I ran [experiments using local models](https://github.com/dcatalanmolina/uxr-local-agents), I learned that this structure works best for smaller models to retrieve files and understand repo structure. And looking to the future, using this naming convention will allow users to transition to more scalable methods to store information when the amount of data grows exponentially.

## Frontmatter Fields

### Data
- `type`: A list with values `Interview`, `Meeting`, `Report`.
- `project`: A link to the corresponding project, `"[[Project A - Overview]]"`. 
- `date`: A date in YYYY-MM-DD format.
- `interviewer`: For interviews, focus groups, or testing sessions, you can add a team member's name.
- `coder`: The name of the team member who coded the datum using Quadro.
- `report-source`: Useful to add links to reports or sources that live outside the vault.

### Codes
- `code description`: A short theme description.

### Insights
- `tags`: A tag for theme category or an different method to organize insights.
- `user-customer`: A list with user or customer profile.
- `project`: A link to the corresponding project, `"[[Project A - Overview]]"`.

### Decisions
- `insights`: A list of links to insights supporting the decision.
- `project`: A link to the corresponding project, `"[[Project A - Overview]]"`.