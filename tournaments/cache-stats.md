# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0082-20261103-122248)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 96 | 4019147 | 3608704 | 89.8% | 90.3% |
| GLM 5.3 Flash | 118 | 5350426 | 4840512 | 90.5% | 90.9% |
| Muse Spark 1.3 | 151 | 6523644 | 6219378 | 95.3% | 95.7% |
| Sonnet 5.5 | 138 | 8001529 | 7211885 | 90.1% | 90.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17073 | 479118034 | 391366402 | 81.7% | 82.0% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7157 | 257952178 | 214923536 | 83.3% | 83.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2832 | 83448438 | 77121084 | 92.4% | 93.0% |
| Sonnet 5.5 | 13509 | 439075832 | 413616197 | 94.2% | 94.8% |
