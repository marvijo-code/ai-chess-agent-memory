# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0004-20261008-185340)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 33 | 303400 | 147328 | 48.6% | 48.4% |
| GPT-6.1 Sol | 22 | 369749 | 331904 | 89.8% | 92.8% |
| Sonnet 5.5 | 43 | 882056 | 839069 | 95.1% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 924 | 10198077 | 4692224 | 46.0% | 45.9% |
| GPT-6.1 Sol | 730 | 20786560 | 19470848 | 93.7% | 94.1% |
| Sonnet 5.5 | 834 | 18980403 | 18184563 | 95.8% | 96.3% |
