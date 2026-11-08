# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0084-20261108-035328)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 60 | 2729936 | 2433280 | 89.1% | 90.8% |
| GLM 5.3 Flash | 75 | 3493042 | 3269440 | 93.6% | 94.0% |
| Muse Spark 1.3 | 52 | 1344724 | 1217441 | 90.5% | 91.6% |
| Sonnet 5.5 | 35 | 2001322 | 1877537 | 93.8% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17534 | 502992230 | 412796290 | 82.1% | 82.4% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7363 | 266630830 | 222820240 | 83.6% | 84.1% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3232 | 99306037 | 91889445 | 92.5% | 93.1% |
| Sonnet 5.5 | 14126 | 476400112 | 448229913 | 94.1% | 94.7% |
