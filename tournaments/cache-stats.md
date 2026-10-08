# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0003-20261008-163034)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 56 | 657189 | 289152 | 44.0% | 43.9% |
| GPT-6.1 Sol | 32 | 642325 | 611968 | 95.3% | 95.9% |
| Sonnet 5.5 | 68 | 1912988 | 1851824 | 96.8% | 97.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 619 | 6958851 | 3470464 | 49.9% | 49.9% |
| GPT-6.1 Sol | 494 | 13805669 | 12814720 | 92.8% | 93.1% |
| Sonnet 5.5 | 631 | 14693248 | 14109787 | 96.0% | 96.5% |
