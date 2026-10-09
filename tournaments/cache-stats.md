# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0008-20261009-055507)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 216 | 2131272 | 924928 | 43.4% | 43.2% |
| GPT-6.1 Sol | 185 | 5096199 | 4718208 | 92.6% | 92.9% |
| Sonnet 5.5 | 171 | 3704836 | 3537115 | 95.5% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2213 | 24623565 | 11225856 | 45.6% | 45.5% |
| GPT-6.1 Sol | 1805 | 53115578 | 49557760 | 93.3% | 93.7% |
| Sonnet 5.5 | 1916 | 43513250 | 41630604 | 95.7% | 96.2% |
