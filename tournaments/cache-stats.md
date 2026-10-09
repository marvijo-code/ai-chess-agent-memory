# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0011-20261009-135256)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 70 | 668700 | 340352 | 50.9% | 50.8% |
| GPT-6.1 Sol | 109 | 3729321 | 3468416 | 93.0% | 93.4% |
| Sonnet 5.5 | 95 | 2283038 | 2190118 | 95.9% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2736 | 29687344 | 13345920 | 45.0% | 44.8% |
| GPT-6.1 Sol | 2446 | 73500226 | 68436608 | 93.1% | 93.5% |
| Sonnet 5.5 | 2499 | 55814192 | 53347975 | 95.6% | 96.2% |
