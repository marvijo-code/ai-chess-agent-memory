# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0034-20261012-050243)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1 | 1 | 1 | 1 | 1 | 2 | 0 | 1 | 0 |
| GLM 5.3 Flash | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
| GPT-6.1 Sol | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| Sonnet 5.5 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 104 | 104 | 104 | 100 | 100 | 170 | 1 | 44 | 4 |
| GLM 5.3 Flash | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
| GPT-6.1 Sol | 111 | 111 | 111 | 111 | 107 | 110 | 4 | 36 | 0 |
| Sonnet 5.5 | 107 | 107 | 106 | 107 | 107 | 98 | 0 | 28 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3 | 14 | 0 |
| GLM 5.3 Flash | 0 | 3 | 0 |
| GPT-6.1 Sol | 3 | 10 | 0 |
| Sonnet 5.5 | 6 | 14 | 0 |
