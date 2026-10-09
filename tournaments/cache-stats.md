# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0012-20261009-164703)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 35 | 277577 | 177536 | 64.0% | 65.0% |
| GPT-6.1 Sol | 43 | 1125799 | 1038976 | 92.3% | 92.9% |
| Sonnet 5.5 | 43 | 858128 | 815815 | 95.1% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2879 | 30962570 | 14013696 | 45.3% | 45.1% |
| GPT-6.1 Sol | 2605 | 77497124 | 72085248 | 93.0% | 93.5% |
| Sonnet 5.5 | 2636 | 58650343 | 56044552 | 95.6% | 96.1% |
