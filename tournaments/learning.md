# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0030-20261011-145519)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3 | 3 | 3 | 3 | 3 | 5 | 0 | 1 | 0 |
| GPT-6.1 Sol | 3 | 3 | 3 | 3 | 3 | 2 | 0 | 0 | 0 |
| Sonnet 5.5 | 3 | 3 | 3 | 3 | 3 | 2 | 0 | 0 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 94 | 94 | 94 | 91 | 91 | 155 | 1 | 39 | 3 |
| GPT-6.1 Sol | 96 | 96 | 96 | 96 | 92 | 95 | 4 | 32 | 0 |
| Sonnet 5.5 | 94 | 94 | 94 | 94 | 94 | 89 | 0 | 26 | 0 |
