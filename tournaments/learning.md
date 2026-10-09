# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0013-20261009-191602)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2 | 2 | 2 | 1 | 1 | 2 | 0 | 1 | 1 |
| GPT-6.1 Sol | 2 | 2 | 2 | 1 | 1 | 1 | 0 | 1 | 0 |
| Sonnet 5.5 | 2 | 2 | 2 | 1 | 1 | 1 | 0 | 1 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7 | 7 | 7 | 6 | 6 | 14 | 0 | 4 | 1 |
| GPT-6.1 Sol | 7 | 7 | 7 | 6 | 4 | 6 | 2 | 4 | 0 |
| Sonnet 5.5 | 7 | 7 | 7 | 6 | 6 | 6 | 0 | 4 | 0 |
