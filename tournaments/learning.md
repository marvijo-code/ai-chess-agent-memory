# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, Fable 5.1: `agents/fable/`, GLM 5.3 Flash: `agents/glm/`, GPT-6 Astra: `agents/astra/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0037-20261012-162646)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4 | 4 | 4 | 4 | 4 | 1 | 0 | 2 | 0 |
| Fable 5.1 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 |
| GLM 5.3 Flash | 3 | 3 | 3 | 3 | 3 | 2 | 0 | 0 | 0 |
| GPT-6 Astra | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 |
| GPT-6.1 Sol | 5 | 5 | 5 | 5 | 4 | 5 | 1 | 6 | 0 |
| Sonnet 5.5 | 4 | 4 | 4 | 4 | 4 | 2 | 0 | 0 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 125 | 125 | 125 | 121 | 120 | 178 | 3 | 62 | 4 |
| Fable 5.1 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 |
| GLM 5.3 Flash | 15 | 15 | 15 | 15 | 15 | 15 | 0 | 4 | 0 |
| GPT-6 Astra | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 |
| GPT-6.1 Sol | 134 | 134 | 134 | 134 | 120 | 133 | 14 | 65 | 0 |
| Sonnet 5.5 | 129 | 129 | 128 | 129 | 129 | 106 | 0 | 36 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 16 | 0 |
| Fable 5.1 | 4 | 16 | 0 |
| GLM 5.3 Flash | 5 | 8 | 0 |
| GPT-6 Astra | 1 | 14 | 0 |
| GPT-6.1 Sol | 2 | 8 | 0 |
| Sonnet 5.5 | 6 | 16 | 0 |
