# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0014-20261009-214817)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 279 | 2893269 | 1468416 | 50.8% | 50.9% |
| GPT-6.1 Sol | 230 | 6844108 | 6454528 | 94.3% | 94.6% |
| Sonnet 5.5 | 200 | 4054193 | 3855101 | 95.1% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3593 | 38933204 | 18032128 | 46.3% | 46.2% |
| GPT-6.1 Sol | 3130 | 91617791 | 85127168 | 92.9% | 93.4% |
| Sonnet 5.5 | 3287 | 73444321 | 70183245 | 95.6% | 96.1% |
