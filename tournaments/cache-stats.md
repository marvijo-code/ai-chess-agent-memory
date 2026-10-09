# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0013-20261009-191602)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 156 | 2051030 | 1066240 | 52.0% | 51.9% |
| GPT-6.1 Sol | 73 | 1808815 | 1575936 | 87.1% | 87.5% |
| Sonnet 5.5 | 89 | 1876003 | 1786170 | 95.2% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3181 | 34401776 | 15787392 | 45.9% | 45.8% |
| GPT-6.1 Sol | 2823 | 83090212 | 77124992 | 92.8% | 93.3% |
| Sonnet 5.5 | 2915 | 65057271 | 62170097 | 95.6% | 96.1% |
