# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0011-20261009-135256)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 87 | 839124 | 465152 | 55.4% | 55.5% |
| GPT-6.1 Sol | 120 | 3875782 | 3597184 | 92.8% | 93.4% |
| Sonnet 5.5 | 114 | 2567667 | 2452661 | 95.5% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2753 | 29857768 | 13470720 | 45.1% | 45.0% |
| GPT-6.1 Sol | 2457 | 73646687 | 68565376 | 93.1% | 93.5% |
| Sonnet 5.5 | 2518 | 56098821 | 53610518 | 95.6% | 96.1% |
