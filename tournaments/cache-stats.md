# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0008-20261009-055507)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 244 | 2359373 | 1016192 | 43.1% | 42.8% |
| GPT-6.1 Sol | 204 | 5397451 | 4988800 | 92.4% | 92.9% |
| Sonnet 5.5 | 222 | 4785744 | 4573030 | 95.6% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2241 | 24851666 | 11317120 | 45.5% | 45.4% |
| GPT-6.1 Sol | 1824 | 53416830 | 49828352 | 93.3% | 93.7% |
| Sonnet 5.5 | 1967 | 44594158 | 42666519 | 95.7% | 96.2% |
