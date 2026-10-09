# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0009-20261009-081556)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 91 | 809387 | 311552 | 38.5% | 37.8% |
| GPT-6.1 Sol | 146 | 5057136 | 4677632 | 92.5% | 93.0% |
| Sonnet 5.5 | 81 | 1416976 | 1329091 | 93.8% | 95.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2351 | 25908737 | 11707904 | 45.2% | 45.1% |
| GPT-6.1 Sol | 1978 | 58689594 | 54691072 | 93.2% | 93.6% |
| Sonnet 5.5 | 2048 | 46011134 | 43995610 | 95.6% | 96.2% |
