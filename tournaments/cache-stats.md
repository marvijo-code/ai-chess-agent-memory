# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0034-20261012-050243)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 67 | 1002563 | 905088 | 90.3% | 91.1% |
| GLM 5.3 Flash | 23 | 168542 | 120320 | 71.4% | 73.3% |
| GPT-6.1 Sol | 76 | 2301437 | 2120448 | 92.1% | 92.9% |
| Sonnet 5.5 | 87 | 2352730 | 2254683 | 95.8% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8609 | 96992364 | 50324352 | 51.9% | 51.8% |
| GLM 5.3 Flash | 23 | 168542 | 120320 | 71.4% | 73.3% |
| GPT-6.1 Sol | 7051 | 206489790 | 192186624 | 93.1% | 93.6% |
| Sonnet 5.5 | 7092 | 157322487 | 150165720 | 95.5% | 96.1% |
