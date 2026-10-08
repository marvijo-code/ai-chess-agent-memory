# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0001-20261008-104409)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 47 | 381146 | 242176 | 63.5% | 64.0% |
| GPT-6.1 Sol | 57 | 1667277 | 1543808 | 92.6% | 93.1% |
| Sonnet 5.5 | 34 | 432320 | 401995 | 93.0% | 93.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 47 | 381146 | 242176 | 63.5% | 64.0% |
| GPT-6.1 Sol | 57 | 1667277 | 1543808 | 92.6% | 93.1% |
| Sonnet 5.5 | 34 | 432320 | 401995 | 93.0% | 93.6% |
