# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0013-20261009-191602)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 206 | 2453290 | 1258624 | 51.3% | 51.2% |
| GPT-6.1 Sol | 110 | 2401512 | 2112896 | 88.0% | 88.8% |
| Sonnet 5.5 | 208 | 4865933 | 4674103 | 96.1% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3231 | 34804036 | 15979776 | 45.9% | 45.8% |
| GPT-6.1 Sol | 2860 | 83682909 | 77661952 | 92.8% | 93.3% |
| Sonnet 5.5 | 3034 | 68047201 | 65058030 | 95.6% | 96.2% |
