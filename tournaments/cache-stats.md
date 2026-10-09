# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0011-20261009-135256)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 76 | 778463 | 417792 | 53.7% | 53.6% |
| GPT-6.1 Sol | 109 | 3729321 | 3468416 | 93.0% | 93.4% |
| Sonnet 5.5 | 100 | 2433062 | 2334615 | 96.0% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2742 | 29797107 | 13423360 | 45.0% | 44.9% |
| GPT-6.1 Sol | 2446 | 73500226 | 68436608 | 93.1% | 93.5% |
| Sonnet 5.5 | 2504 | 55964216 | 53492472 | 95.6% | 96.2% |
