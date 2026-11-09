# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0086-20261108-185025)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 223 | 13801411 | 12949888 | 93.8% | 94.3% |
| GLM 5.3 Flash | 89 | 3752131 | 3445696 | 91.8% | 92.4% |
| Muse Spark 1.3 | 114 | 4024737 | 3621194 | 90.0% | 90.4% |
| Sonnet 5.5 | 165 | 8971634 | 8363458 | 93.2% | 93.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18102 | 535623345 | 443099138 | 82.7% | 83.1% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7736 | 282294431 | 236938128 | 83.9% | 84.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3701 | 114965321 | 106355105 | 92.5% | 93.1% |
| Sonnet 5.5 | 14830 | 514932930 | 484262430 | 94.0% | 94.6% |
