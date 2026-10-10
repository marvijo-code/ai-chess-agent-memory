# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0020-20261010-134348)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 29 | 210318 | 87040 | 41.4% | 41.0% |
| GPT-6.1 Sol | 25 | 502545 | 438912 | 87.3% | 90.0% |
| Sonnet 5.5 | 17 | 193943 | 172612 | 89.0% | 91.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5108 | 55897304 | 26564992 | 47.5% | 47.5% |
| GPT-6.1 Sol | 4147 | 119931874 | 111374080 | 92.9% | 93.3% |
| Sonnet 5.5 | 4366 | 96141058 | 91808915 | 95.5% | 96.1% |
