# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0023-20261010-213538)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 130 | 1556072 | 972800 | 62.5% | 62.8% |
| GPT-6.1 Sol | 76 | 2022818 | 1860480 | 92.0% | 92.5% |
| Sonnet 5.5 | 80 | 1601992 | 1519157 | 94.8% | 95.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6025 | 67059543 | 33223168 | 49.5% | 49.5% |
| GPT-6.1 Sol | 4850 | 139689289 | 129922688 | 93.0% | 93.5% |
| Sonnet 5.5 | 5112 | 113031295 | 107954860 | 95.5% | 96.1% |
