# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0031-20261011-172532)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5 | 5 | 5 | 3 | 3 | 6 | 0 | 0 | 1 |
| GPT-6.1 Sol | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| Sonnet 5.5 | 5 | 5 | 5 | 4 | 4 | 3 | 0 | 0 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 101 | 101 | 101 | 96 | 96 | 163 | 1 | 40 | 4 |
| GPT-6.1 Sol | 103 | 103 | 103 | 103 | 99 | 102 | 4 | 32 | 0 |
| Sonnet 5.5 | 101 | 101 | 101 | 100 | 100 | 93 | 0 | 26 | 0 |
