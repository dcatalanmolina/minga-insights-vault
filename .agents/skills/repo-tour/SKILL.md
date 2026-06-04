---
name: repo-tour
description: Use when the user needs help understanding how to use the minga-insights-vault repo.
---

Help the user to get started with the repo by following the instructions below.

# Instructions

## 1. Welcome
Print the following welcome message to start the conversation:

```
Welcome to minga-insights-vault!

What do you want to accomplish today? Select a number to get started:

1. I'm new here. I'd like to understand the folder structure and content in this repo. 

2. I'm not new, but I feel lost. I'd like to gain more clarity on how I may use this repo.

3. I know my way around the repo; I just have a specific question. 
```

## 2. Detect Goal
The user's choice reveals your goal for this session:

| Selection | Goal |
|----------------|-------------------------------|
| 1 | Walk them through the folder structure first. Ask follow-up questions to ensure they understand the purpose of each folder. |
| 2 | Ask the user what they do understand about the repo first to check for misunderstandings. Then, ask if you can help them complete small tasks (e.g., adding an interview file to the Data folder or describing a project) to get the ball rolling. |