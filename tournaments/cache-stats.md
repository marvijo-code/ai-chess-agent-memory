# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0036-20261012-121058)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16 | 181176 | 132864 | 73.3% | 78.1% |
| GLM 5.3 Flash | 29 | 321112 | 283264 | 88.2% | 89.3% |
| Sonnet 5.5 | 15 | 238847 | 215305 | 90.1% | 94.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8893 | 101366495 | 54276864 | 53.5% | 53.5% |
| GLM 5.3 Flash | 317 | 4105605 | 3522112 | 85.8% | 86.5% |
| GPT-6.1 Sol | 7424 | 217510756 | 202383104 | 93.0% | 93.5% |
| Sonnet 5.5 | 7596 | 170775318 | 163072267 | 95.5% | 96.2% |
