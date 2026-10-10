# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0017-20261010-051708)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4 | 4 | 4 | 4 | 4 | 5 | 0 | 1 | 0 |
| GPT-6.1 Sol | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 |
| Sonnet 5.5 | 3 | 3 | 3 | 3 | 3 | 2 | 0 | 1 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 29 | 29 | 29 | 28 | 28 | 50 | 0 | 8 | 1 |
| GPT-6.1 Sol | 29 | 29 | 29 | 29 | 25 | 29 | 4 | 17 | 0 |
| Sonnet 5.5 | 28 | 28 | 28 | 28 | 28 | 27 | 0 | 8 | 0 |
