# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0003-20261008-163034)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 328 | 3593015 | 1363584 | 38.0% | 37.7% |
| GPT-6.1 Sol | 246 | 7253467 | 6936192 | 95.6% | 96.0% |
| Sonnet 5.5 | 228 | 5318087 | 5087531 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 891 | 9894677 | 4544896 | 45.9% | 45.9% |
| GPT-6.1 Sol | 708 | 20416811 | 19138944 | 93.7% | 94.1% |
| Sonnet 5.5 | 791 | 18098347 | 17345494 | 95.8% | 96.3% |
