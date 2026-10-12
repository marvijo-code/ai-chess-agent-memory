# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0035-20261012-085617)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4 | 4 | 4 | 4 | 3 | 1 | 2 | 3 | 0 |
| GLM 5.3 Flash | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 1 | 0 |
| GPT-6.1 Sol | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 2 | 0 |
| Sonnet 5.5 | 3 | 3 | 3 | 3 | 3 | 1 | 0 | 2 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 113 | 113 | 113 | 109 | 108 | 174 | 3 | 53 | 4 |
| GLM 5.3 Flash | 7 | 7 | 7 | 7 | 7 | 8 | 0 | 2 | 0 |
| GPT-6.1 Sol | 119 | 119 | 119 | 119 | 114 | 118 | 5 | 40 | 0 |
| Sonnet 5.5 | 116 | 116 | 115 | 116 | 116 | 102 | 0 | 33 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 16 | 0 |
| GLM 5.3 Flash | 1 | 9 | 0 |
| GPT-6.1 Sol | 3 | 10 | 0 |
| Sonnet 5.5 | 2 | 14 | 0 |
