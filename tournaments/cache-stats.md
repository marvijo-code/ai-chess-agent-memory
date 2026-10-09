# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0008-20261009-055507)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 205 | 1945186 | 800256 | 41.1% | 40.8% |
| GPT-6.1 Sol | 185 | 5096199 | 4718208 | 92.6% | 92.9% |
| Sonnet 5.5 | 162 | 3460260 | 3300474 | 95.4% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2202 | 24437479 | 11101184 | 45.4% | 45.3% |
| GPT-6.1 Sol | 1805 | 53115578 | 49557760 | 93.3% | 93.7% |
| Sonnet 5.5 | 1907 | 43268674 | 41393963 | 95.7% | 96.2% |
