# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0088-20261109-135130)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 33 | 1577235 | 1429376 | 90.6% | 91.1% |
| GLM 5.3 Flash | 32 | 1532840 | 1272960 | 83.0% | 83.5% |
| Muse Spark 1.3 | 61 | 3261840 | 3148555 | 96.5% | 96.8% |
| Sonnet 5.5 | 56 | 3398626 | 3162406 | 93.0% | 93.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18478 | 556737425 | 462490626 | 83.1% | 83.4% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 8106 | 299641785 | 252662992 | 84.3% | 84.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 4041 | 131489769 | 122038407 | 92.8% | 93.4% |
| Sonnet 5.5 | 15106 | 531474586 | 499791442 | 94.0% | 94.6% |
