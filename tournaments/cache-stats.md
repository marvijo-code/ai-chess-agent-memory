# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0006-20261009-001831)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 158 | 2164747 | 1005568 | 46.5% | 46.3% |
| GPT-6.1 Sol | 73 | 1737624 | 1545472 | 88.9% | 89.8% |
| Sonnet 5.5 | 97 | 2265516 | 2166088 | 95.6% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1552 | 17534338 | 8066304 | 46.0% | 45.9% |
| GPT-6.1 Sol | 1243 | 36576278 | 34141184 | 93.3% | 93.8% |
| Sonnet 5.5 | 1323 | 30254756 | 28961186 | 95.7% | 96.2% |
