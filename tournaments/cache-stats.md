# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0014-20261009-214817)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 241 | 2553174 | 1321344 | 51.8% | 52.0% |
| GPT-6.1 Sol | 195 | 5868698 | 5566720 | 94.9% | 95.2% |
| Sonnet 5.5 | 177 | 3760695 | 3587493 | 95.4% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3555 | 38593109 | 17885056 | 46.3% | 46.3% |
| GPT-6.1 Sol | 3095 | 90642381 | 84239360 | 92.9% | 93.4% |
| Sonnet 5.5 | 3264 | 73150823 | 69915637 | 95.6% | 96.2% |
