# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0043-20261016-140539)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 23 | 1110043 | 947712 | 85.4% | 85.8% |
| GLM 5.3 Flash | 20 | 684759 | 592960 | 86.6% | 87.5% |
| GPT-6.1 Sol | 21 | 445796 | 404736 | 90.8% | 92.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10383 | 129447307 | 80025600 | 61.8% | 61.9% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1419 | 24538141 | 21580352 | 87.9% | 88.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9342 | 282090854 | 262413056 | 93.0% | 93.6% |
| Sonnet 5.5 | 9731 | 234697344 | 224635504 | 95.7% | 96.4% |
