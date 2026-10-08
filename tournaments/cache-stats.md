# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0001-20261008-104409)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 74 | 575769 | 347520 | 60.4% | 60.8% |
| GPT-6.1 Sol | 77 | 1975082 | 1808384 | 91.6% | 92.1% |
| Sonnet 5.5 | 79 | 1226093 | 1155251 | 94.2% | 94.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 74 | 575769 | 347520 | 60.4% | 60.8% |
| GPT-6.1 Sol | 77 | 1975082 | 1808384 | 91.6% | 92.1% |
| Sonnet 5.5 | 79 | 1226093 | 1155251 | 94.2% | 94.7% |
