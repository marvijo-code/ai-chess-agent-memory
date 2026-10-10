# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0016-20261010-025717)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 214 | 2246371 | 1213696 | 54.0% | 54.1% |
| GPT-6.1 Sol | 141 | 3037453 | 2723712 | 89.7% | 90.6% |
| Sonnet 5.5 | 143 | 2304675 | 2155061 | 93.5% | 94.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4128 | 44875146 | 21028608 | 46.9% | 46.8% |
| GPT-6.1 Sol | 3497 | 101343514 | 94150656 | 92.9% | 93.4% |
| Sonnet 5.5 | 3664 | 80802933 | 77162408 | 95.5% | 96.1% |
