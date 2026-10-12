# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0034-20261012-050243)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 93 | 1336509 | 1209984 | 90.5% | 91.5% |
| GLM 5.3 Flash | 84 | 808295 | 643840 | 79.7% | 80.7% |
| GPT-6.1 Sol | 106 | 3003337 | 2768128 | 92.2% | 92.9% |
| Sonnet 5.5 | 181 | 4889522 | 4695231 | 96.0% | 97.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8635 | 97326310 | 50629248 | 52.0% | 52.0% |
| GLM 5.3 Flash | 84 | 808295 | 643840 | 79.7% | 80.7% |
| GPT-6.1 Sol | 7081 | 207191690 | 192834304 | 93.1% | 93.5% |
| Sonnet 5.5 | 7186 | 159859279 | 152606268 | 95.5% | 96.1% |
