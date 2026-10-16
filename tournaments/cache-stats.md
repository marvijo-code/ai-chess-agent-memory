# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0043-20261016-140539)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 23 | 1110043 | 947712 | 85.4% | 85.8% |
| GLM 5.3 Flash | 29 | 1403720 | 1256000 | 89.5% | 89.9% |
| GPT-6.1 Sol | 29 | 728805 | 679168 | 93.2% | 94.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10383 | 129447307 | 80025600 | 61.8% | 61.9% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1428 | 25257102 | 22243392 | 88.1% | 88.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9350 | 282373863 | 262687488 | 93.0% | 93.6% |
| Sonnet 5.5 | 9731 | 234697344 | 224635504 | 95.7% | 96.4% |
