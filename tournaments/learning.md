# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0015-20261010-001334)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5 | 5 | 5 | 5 | 5 | 9 | 0 | 0 | 0 |
| GPT-6.1 Sol | 5 | 5 | 5 | 5 | 4 | 5 | 1 | 3 | 0 |
| Sonnet 5.5 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 1 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 20 | 20 | 20 | 19 | 19 | 37 | 0 | 6 | 1 |
| GPT-6.1 Sol | 20 | 20 | 20 | 20 | 16 | 20 | 4 | 15 | 0 |
| Sonnet 5.5 | 20 | 20 | 20 | 20 | 20 | 20 | 0 | 7 | 0 |
