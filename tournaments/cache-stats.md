# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0008-20261009-055507)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 38 | 281032 | 101248 | 36.0% | 35.2% |
| GPT-6.1 Sol | 49 | 1460430 | 1361280 | 93.2% | 93.4% |
| Sonnet 5.5 | 20 | 242932 | 220147 | 90.6% | 92.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2035 | 22773325 | 10402176 | 45.7% | 45.6% |
| GPT-6.1 Sol | 1669 | 49479809 | 46200832 | 93.4% | 93.8% |
| Sonnet 5.5 | 1765 | 40051346 | 38313636 | 95.7% | 96.2% |
