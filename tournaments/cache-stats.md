# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 78 | 947644 | 433536 | 45.7% | 45.6% |
| GPT-6.1 Sol | 42 | 1033936 | 990592 | 95.8% | 96.2% |
| Sonnet 5.5 | 70 | 2057304 | 1993334 | 96.9% | 97.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 315 | 3283742 | 1710208 | 52.1% | 52.2% |
| GPT-6.1 Sol | 344 | 10587950 | 9894656 | 93.5% | 93.7% |
| Sonnet 5.5 | 339 | 7662984 | 7355139 | 96.0% | 96.4% |
