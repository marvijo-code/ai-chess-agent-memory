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
| DeepSeek V4.1 Flash | 4 | 4 | 4 | 4 | 4 | 4 | 0 | 5 | 0 |
| GLM 5.3 Flash | 4 | 4 | 4 | 4 | 4 | 5 | 0 | 1 | 0 |
| GPT-6.1 Sol | 4 | 4 | 4 | 4 | 3 | 4 | 1 | 2 | 0 |
| Sonnet 5.5 | 4 | 4 | 4 | 4 | 4 | 1 | 0 | 2 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 107 | 107 | 107 | 103 | 103 | 172 | 1 | 48 | 4 |
| GLM 5.3 Flash | 4 | 4 | 4 | 4 | 4 | 5 | 0 | 1 | 0 |
| GPT-6.1 Sol | 114 | 114 | 114 | 114 | 109 | 113 | 5 | 38 | 0 |
| Sonnet 5.5 | 110 | 110 | 109 | 110 | 110 | 99 | 0 | 30 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5 | 16 | 0 |
| GLM 5.3 Flash | 1 | 8 | 0 |
| GPT-6.1 Sol | 3 | 10 | 0 |
| Sonnet 5.5 | 5 | 14 | 0 |
