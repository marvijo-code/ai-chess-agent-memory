# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 235 | 2806610 | 1281408 | 45.7% | 45.5% |
| GPT-6.1 Sol | 123 | 2746234 | 2506368 | 91.3% | 91.8% |
| Sonnet 5.5 | 165 | 3809512 | 3647785 | 95.8% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 472 | 5142708 | 2558080 | 49.7% | 49.8% |
| GPT-6.1 Sol | 425 | 12300248 | 11410432 | 92.8% | 93.1% |
| Sonnet 5.5 | 434 | 9415192 | 9009590 | 95.7% | 96.2% |
