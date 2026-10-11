# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0027-20261011-075651)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5 | 5 | 5 | 5 | 5 | 10 | 0 | 3 | 0 |
| GPT-6.1 Sol | 6 | 6 | 6 | 6 | 6 | 6 | 0 | 1 | 0 |
| Sonnet 5.5 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 1 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 81 | 81 | 81 | 78 | 78 | 132 | 1 | 35 | 3 |
| GPT-6.1 Sol | 83 | 83 | 83 | 83 | 79 | 83 | 4 | 29 | 0 |
| Sonnet 5.5 | 81 | 81 | 81 | 81 | 81 | 75 | 0 | 23 | 0 |
