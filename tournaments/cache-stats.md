# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0021-20261010-172846)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 285 | 3406779 | 2123264 | 62.3% | 62.3% |
| GPT-6.1 Sol | 195 | 5075791 | 4803840 | 94.6% | 95.0% |
| Sonnet 5.5 | 169 | 3179579 | 2995764 | 94.2% | 95.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5659 | 63064091 | 30910976 | 49.0% | 49.0% |
| GPT-6.1 Sol | 4626 | 134494385 | 125133312 | 93.0% | 93.5% |
| Sonnet 5.5 | 4850 | 107719825 | 102919277 | 95.5% | 96.1% |
