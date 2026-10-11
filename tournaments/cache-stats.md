# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0030-20261011-145519)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 43 | 376691 | 159232 | 42.3% | 41.9% |
| GPT-6.1 Sol | 62 | 2294398 | 2166272 | 94.4% | 94.8% |
| Sonnet 5.5 | 62 | 1692396 | 1635375 | 96.6% | 97.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7867 | 87763058 | 44949504 | 51.2% | 51.2% |
| GPT-6.1 Sol | 6288 | 182918997 | 170368640 | 93.1% | 93.6% |
| Sonnet 5.5 | 6437 | 141054476 | 134630825 | 95.4% | 96.1% |
