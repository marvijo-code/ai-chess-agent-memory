# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0006-20261009-001831)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 296 | 3501519 | 1683328 | 48.1% | 47.9% |
| GPT-6.1 Sol | 196 | 5200015 | 4784640 | 92.0% | 92.5% |
| Sonnet 5.5 | 251 | 5843269 | 5593324 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1690 | 18871110 | 8744064 | 46.3% | 46.2% |
| GPT-6.1 Sol | 1366 | 40038669 | 37380352 | 93.4% | 93.8% |
| Sonnet 5.5 | 1477 | 33832509 | 32388422 | 95.7% | 96.2% |
