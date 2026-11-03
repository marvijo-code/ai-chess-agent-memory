# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0081-20261103-045347)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| GLM 5.3 Flash | 15 | 227303 | 191488 | 84.2% | 86.8% |
| Muse Spark 1.3 | 6 | 62702 | 48309 | 77.0% | 88.2% |
| Sonnet 5.5 | 13 | 364633 | 317613 | 87.1% | 90.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16751 | 463734150 | 377399298 | 81.4% | 81.7% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6890 | 245095893 | 203345040 | 83.0% | 83.5% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2524 | 72128312 | 66765340 | 92.6% | 93.2% |
| Sonnet 5.5 | 13117 | 417689296 | 394134014 | 94.4% | 95.0% |
