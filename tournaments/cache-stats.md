# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0075-20261029-072421)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 291 | 15393056 | 14006144 | 91.0% | 91.2% |
| GLM 5.3 Flash | 136 | 5944741 | 5182144 | 87.2% | 87.6% |
| Muse Spark 1.3 | 258 | 8325497 | 7554401 | 90.7% | 91.2% |
| Sonnet 5.5 | 309 | 17040740 | 15860247 | 93.1% | 93.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15405 | 390917003 | 311734274 | 79.7% | 80.0% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5931 | 198595125 | 161679940 | 81.4% | 82.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1534 | 37144639 | 34423939 | 92.7% | 93.2% |
| Sonnet 5.5 | 11809 | 345288189 | 327703492 | 94.9% | 95.5% |
