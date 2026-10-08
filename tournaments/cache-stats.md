# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 325 | 3944518 | 1884160 | 47.8% | 47.7% |
| GPT-6.1 Sol | 159 | 3568106 | 3259008 | 91.3% | 91.8% |
| Sonnet 5.5 | 261 | 6644990 | 6400699 | 96.3% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 562 | 6280616 | 3160832 | 50.3% | 50.3% |
| GPT-6.1 Sol | 461 | 13122120 | 12163072 | 92.7% | 93.0% |
| Sonnet 5.5 | 530 | 12250670 | 11762504 | 96.0% | 96.4% |
