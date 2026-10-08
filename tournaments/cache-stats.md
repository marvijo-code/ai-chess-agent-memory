# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0001-20261008-104409)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 156 | 1229175 | 657536 | 53.5% | 53.8% |
| GPT-6.1 Sol | 252 | 8016473 | 7494656 | 93.5% | 93.7% |
| Sonnet 5.5 | 245 | 5328114 | 5107419 | 95.9% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 156 | 1229175 | 657536 | 53.5% | 53.8% |
| GPT-6.1 Sol | 252 | 8016473 | 7494656 | 93.5% | 93.7% |
| Sonnet 5.5 | 245 | 5328114 | 5107419 | 95.9% | 96.2% |
