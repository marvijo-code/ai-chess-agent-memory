# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0003-20261008-163034)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 292 | 3145254 | 1288832 | 41.0% | 40.8% |
| GPT-6.1 Sol | 233 | 6934323 | 6655488 | 96.0% | 96.4% |
| Sonnet 5.5 | 228 | 5318087 | 5087531 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 855 | 9446916 | 4470144 | 47.3% | 47.3% |
| GPT-6.1 Sol | 695 | 20097667 | 18858240 | 93.8% | 94.2% |
| Sonnet 5.5 | 791 | 18098347 | 17345494 | 95.8% | 96.3% |
