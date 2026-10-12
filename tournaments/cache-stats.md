# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0034-20261012-050243)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 67 | 1002563 | 905088 | 90.3% | 91.1% |
| GLM 5.3 Flash | 23 | 168542 | 120320 | 71.4% | 73.3% |
| GPT-6.1 Sol | 47 | 976806 | 859520 | 88.0% | 89.5% |
| Sonnet 5.5 | 57 | 1224053 | 1152191 | 94.1% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8609 | 96992364 | 50324352 | 51.9% | 51.8% |
| GLM 5.3 Flash | 23 | 168542 | 120320 | 71.4% | 73.3% |
| GPT-6.1 Sol | 7022 | 205165159 | 190925696 | 93.1% | 93.5% |
| Sonnet 5.5 | 7062 | 156193810 | 149063228 | 95.4% | 96.1% |
