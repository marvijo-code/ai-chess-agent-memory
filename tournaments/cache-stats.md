# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0014-20261009-214817)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 99 | 1017496 | 504448 | 49.6% | 49.8% |
| GPT-6.1 Sol | 98 | 3102911 | 2976000 | 95.9% | 96.2% |
| Sonnet 5.5 | 81 | 1682719 | 1599149 | 95.0% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3413 | 37057431 | 17068160 | 46.1% | 46.0% |
| GPT-6.1 Sol | 2998 | 87876594 | 81648640 | 92.9% | 93.4% |
| Sonnet 5.5 | 3168 | 71072847 | 67927293 | 95.6% | 96.1% |
