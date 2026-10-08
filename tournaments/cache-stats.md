# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 273 | 3330602 | 1500928 | 45.1% | 45.0% |
| GPT-6.1 Sol | 123 | 2746234 | 2506368 | 91.3% | 91.8% |
| Sonnet 5.5 | 180 | 4158450 | 3980723 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 510 | 5666700 | 2777600 | 49.0% | 49.0% |
| GPT-6.1 Sol | 425 | 12300248 | 11410432 | 92.8% | 93.1% |
| Sonnet 5.5 | 449 | 9764130 | 9342528 | 95.7% | 96.2% |
