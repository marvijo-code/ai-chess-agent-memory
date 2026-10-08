# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 63 | 657818 | 220032 | 33.4% | 33.1% |
| GPT-6.1 Sol | 30 | 582847 | 552832 | 94.9% | 95.5% |
| Sonnet 5.5 | 70 | 2057304 | 1993334 | 96.9% | 97.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 300 | 2993916 | 1496704 | 50.0% | 50.0% |
| GPT-6.1 Sol | 332 | 10136861 | 9456896 | 93.3% | 93.5% |
| Sonnet 5.5 | 339 | 7662984 | 7355139 | 96.0% | 96.4% |
