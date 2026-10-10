# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0023-20261010-213538)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1 | 1 | 1 | 1 | 1 | 2 | 0 | 0 | 0 |
| GPT-6.1 Sol | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 |
| Sonnet 5.5 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 57 | 57 | 57 | 55 | 55 | 90 | 1 | 21 | 2 |
| GPT-6.1 Sol | 59 | 59 | 59 | 59 | 55 | 59 | 4 | 24 | 0 |
| Sonnet 5.5 | 57 | 57 | 57 | 57 | 57 | 55 | 0 | 15 | 0 |
