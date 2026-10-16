# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0042-20261016-110957)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 37 | 502257 | 423296 | 84.3% | 84.8% |
| GLM 5.3 Flash | 10 | 85990 | 70720 | 82.2% | 88.9% |
| GPT-6.1 Sol | 14 | 253385 | 235392 | 92.9% | 95.6% |
| Sonnet 5.5 | 66 | 1563162 | 1477187 | 94.5% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10280 | 127219540 | 78132608 | 61.4% | 61.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1313 | 22544822 | 19887360 | 88.2% | 88.9% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9180 | 277036540 | 257788416 | 93.1% | 93.6% |
| Sonnet 5.5 | 9599 | 230649664 | 220736467 | 95.7% | 96.4% |
