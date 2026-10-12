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
| DeepSeek V4.1 Flash | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 1 | 0 |
| Fable 5.1 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 |
| GLM 5.3 Flash | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 |
| GPT-6 Astra | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 |
| GPT-6.1 Sol | 3 | 3 | 3 | 3 | 2 | 3 | 1 | 5 | 0 |
| Sonnet 5.5 | 4 | 4 | 4 | 4 | 4 | 2 | 0 | 0 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 123 | 123 | 123 | 119 | 118 | 177 | 3 | 61 | 4 |
| Fable 5.1 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 |
| GLM 5.3 Flash | 14 | 14 | 14 | 14 | 14 | 15 | 0 | 4 | 0 |
| GPT-6 Astra | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 |
| GPT-6.1 Sol | 132 | 132 | 132 | 132 | 118 | 131 | 14 | 64 | 0 |
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
