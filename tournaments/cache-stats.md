# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0036-20261012-121058)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 59 | 847373 | 749440 | 88.4% | 90.2% |
| GLM 5.3 Flash | 29 | 321112 | 283264 | 88.2% | 89.3% |
| GPT-6.1 Sol | 29 | 713350 | 662784 | 92.9% | 93.7% |
| Sonnet 5.5 | 56 | 1188669 | 1116010 | 93.9% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8936 | 102032692 | 54893440 | 53.8% | 53.8% |
| GLM 5.3 Flash | 317 | 4105605 | 3522112 | 85.8% | 86.5% |
| GPT-6.1 Sol | 7453 | 218224106 | 203045888 | 93.0% | 93.5% |
| Sonnet 5.5 | 7637 | 171725140 | 163972972 | 95.5% | 96.2% |
