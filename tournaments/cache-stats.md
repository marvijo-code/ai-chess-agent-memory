# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0079-20261102-080217)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 168 | 8925900 | 8332032 | 93.3% | 93.7% |
| GLM 5.3 Flash | 146 | 6111374 | 5369280 | 87.9% | 88.3% |
| Muse Spark 1.3 | 113 | 3263945 | 3024315 | 92.7% | 93.6% |
| Sonnet 5.5 | 129 | 6473141 | 5937021 | 91.7% | 92.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16408 | 446300531 | 361780610 | 81.1% | 81.3% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6768 | 240755760 | 199575120 | 82.9% | 83.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2291 | 64832335 | 60077523 | 92.7% | 93.2% |
| Sonnet 5.5 | 12701 | 396183824 | 374653266 | 94.6% | 95.2% |
