# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0020-20261010-134348)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5 | 5 | 5 | 5 | 5 | 9 | 0 | 4 | 0 |
| GPT-6.1 Sol | 6 | 6 | 6 | 6 | 6 | 6 | 0 | 2 | 0 |
| Sonnet 5.5 | 6 | 6 | 6 | 6 | 6 | 7 | 0 | 1 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 46 | 46 | 46 | 45 | 45 | 75 | 0 | 17 | 1 |
| GPT-6.1 Sol | 47 | 47 | 47 | 47 | 43 | 47 | 4 | 22 | 0 |
| Sonnet 5.5 | 46 | 46 | 46 | 46 | 46 | 46 | 0 | 11 | 0 |
