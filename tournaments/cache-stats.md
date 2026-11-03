# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0081-20261103-045347)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 32 | 718100 | 618624 | 86.1% | 87.8% |
| GLM 5.3 Flash | 124 | 5698428 | 5421504 | 95.1% | 95.5% |
| Muse Spark 1.3 | 25 | 453697 | 403751 | 89.0% | 92.3% |
| Sonnet 5.5 | 142 | 8030004 | 7387622 | 92.0% | 92.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16783 | 464452250 | 378017922 | 81.4% | 81.7% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6999 | 250567018 | 208575056 | 83.2% | 83.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2543 | 72519307 | 67120782 | 92.6% | 93.2% |
| Sonnet 5.5 | 13246 | 425354667 | 401204023 | 94.3% | 94.9% |
