# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0019-20261010-104326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 261 | 2526677 | 1038848 | 41.1% | 40.9% |
| GPT-6.1 Sol | 229 | 7249021 | 6775040 | 93.5% | 93.8% |
| Sonnet 5.5 | 204 | 4603379 | 4401955 | 95.6% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5061 | 55423943 | 26332928 | 47.5% | 47.4% |
| GPT-6.1 Sol | 4122 | 119429329 | 110935168 | 92.9% | 93.4% |
| Sonnet 5.5 | 4338 | 95671468 | 91373276 | 95.5% | 96.1% |
