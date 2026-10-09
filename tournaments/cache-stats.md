# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0006-20261009-001831)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 261 | 3188245 | 1517696 | 47.6% | 47.5% |
| GPT-6.1 Sol | 174 | 4831029 | 4452224 | 92.2% | 92.6% |
| Sonnet 5.5 | 199 | 4700193 | 4498742 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1655 | 18557836 | 8578432 | 46.2% | 46.1% |
| GPT-6.1 Sol | 1344 | 39669683 | 37047936 | 93.4% | 93.8% |
| Sonnet 5.5 | 1425 | 32689433 | 31293840 | 95.7% | 96.2% |
