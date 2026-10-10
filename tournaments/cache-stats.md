# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0022-20261010-192853)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 96 | 914897 | 494080 | 54.0% | 53.8% |
| GPT-6.1 Sol | 47 | 857459 | 772096 | 90.0% | 90.6% |
| Sonnet 5.5 | 52 | 787766 | 728604 | 92.5% | 94.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5755 | 63978988 | 31405056 | 49.1% | 49.0% |
| GPT-6.1 Sol | 4673 | 135351844 | 125905408 | 93.0% | 93.5% |
| Sonnet 5.5 | 4902 | 108507591 | 103647881 | 95.5% | 96.1% |
