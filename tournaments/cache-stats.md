# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0036-20261012-121058)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 29 | 415851 | 360576 | 86.7% | 89.3% |
| GLM 5.3 Flash | 29 | 321112 | 283264 | 88.2% | 89.3% |
| Sonnet 5.5 | 29 | 608164 | 571672 | 94.0% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8906 | 101601170 | 54504576 | 53.6% | 53.6% |
| GLM 5.3 Flash | 317 | 4105605 | 3522112 | 85.8% | 86.5% |
| GPT-6.1 Sol | 7424 | 217510756 | 202383104 | 93.0% | 93.5% |
| Sonnet 5.5 | 7610 | 171144635 | 163428634 | 95.5% | 96.2% |
