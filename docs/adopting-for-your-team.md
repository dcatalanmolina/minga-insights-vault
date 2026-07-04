# Adopting This Repo for Your Team

A guide for taking your own private copy of `minga-insights-vault`, sharing it with a GitHub Team, and pulling in new releases as they ship.

## 1. Get your own copy

The repo is MIT-licensed, so cloning, modifying, and keeping a private copy is fine. The recommended way to do it is a **mirror clone** — it gives you a fully independent private repo while preserving the entire commit history, which matters for step 3.

```bash
# 1. Mirror the public repo (includes all branches, tags, and history)
git clone --mirror https://github.com/dcatalanmolina/minga-insights-vault.git

# 2. Create an empty private repo under your account or org
gh repo create your-org/your-insights-vault --private

# 3. Push the mirror into it
cd minga-insights-vault.git
git push https://github.com/your-org/your-insights-vault.git --mirror
```

You now have a private repo with full history, unconnected to GitHub's fork network — no "Fork" badge, no visibility restrictions.

**Alternative:** if a "Use this template" button is ever added to this repo, that also produces a repo of your chosen visibility, but starts from a single fresh commit with no shared history. That makes step 3 (pulling updates) much harder, so the mirror method above is preferred if you plan to stay in sync with future releases.

## 2. Share it with your Team

Grant access the normal GitHub way — this is unrelated to which cloning method you used above:

1. In your org, go to the new repo's **Settings → Collaborators and teams**.
2. Add the relevant GitHub **Team** and set its permission level (Write is usually enough for a research team using the vault day to day).

## 3. Keep your content separate from the "product"

Day-to-day work — interview data, analyses, insights, decisions, workflow canvases — lives in `Data/`, `Analysis/`, `Codes/`, `Decisions/`, `Global Notes/`, `Projects/`, and `Workflows/`. These are yours to fill freely.

The "product" itself — agent definitions, skills, and docs — lives in `.agents/` and `docs/`. Avoid heavy edits there unless you intend to fork the project's direction, not just use it. Keeping this separation is what makes step 4 low-friction: upstream changes land in folders you rarely touch, so merges stay clean.

**You are more than welcome to suggest changes as bug reports or feature requests**. These changes may benefit every team using the repo and will avoid you having to manually edit files every time you want to pull a new release.

## 4. Pull in new releases

Add the original repo as a second remote, once:

```bash
git remote add upstream https://github.com/dcatalanmolina/minga-insights-vault.git
```

Then, whenever a new release ships:

```bash
git fetch upstream --tags
git merge upstream/main        # take the latest, or...
git merge v0.4.0                # ...pin to a specific tagged release
```

Because your copy shares full history with upstream (thanks to the mirror clone in step 1), Git can do a real three-way merge. Conflicts should only surface where you've edited a file upstream also changed — rare if you've kept customizations inside your own data folders as described in step 3.

Check the [Releases page](https://github.com/dcatalanmolina/minga-insights-vault/releases) to see what changed before merging.
