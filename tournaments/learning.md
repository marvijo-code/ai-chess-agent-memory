# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0015-20261010-001334)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3 | 3 | 3 | 3 | 3 | 6 | 0 | 0 | 0 |
| GPT-6.1 Sol | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 |
| Sonnet 5.5 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18 | 18 | 18 | 17 | 17 | 34 | 0 | 6 | 1 |
| GPT-6.1 Sol | 17 | 17 | 17 | 17 | 14 | 17 | 3 | 12 | 0 |
| Sonnet 5.5 | 17 | 17 | 17 | 17 | 17 | 17 | 0 | 6 | 0 |
