# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0006-20261009-001831)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 310 | 3709943 | 1773440 | 47.8% | 47.7% |
| GPT-6.1 Sol | 204 | 5428045 | 5003648 | 92.2% | 92.7% |
| Sonnet 5.5 | 285 | 6482690 | 6193643 | 95.5% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1704 | 19079534 | 8834176 | 46.3% | 46.2% |
| GPT-6.1 Sol | 1374 | 40266699 | 37599360 | 93.4% | 93.8% |
| Sonnet 5.5 | 1511 | 34471930 | 32988741 | 95.7% | 96.2% |
