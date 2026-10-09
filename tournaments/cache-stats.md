# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0009-20261009-081556)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 60 | 426031 | 193536 | 45.4% | 44.7% |
| GPT-6.1 Sol | 130 | 4675562 | 4333056 | 92.7% | 93.2% |
| Sonnet 5.5 | 81 | 1416976 | 1329091 | 93.8% | 95.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2320 | 25525381 | 11589888 | 45.4% | 45.3% |
| GPT-6.1 Sol | 1962 | 58308020 | 54346496 | 93.2% | 93.6% |
| Sonnet 5.5 | 2048 | 46011134 | 43995610 | 95.6% | 96.2% |
