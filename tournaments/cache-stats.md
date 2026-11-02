# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0079-20261102-080217)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 77 | 4176140 | 3891584 | 93.2% | 93.5% |
| GLM 5.3 Flash | 55 | 1945048 | 1677696 | 86.3% | 86.9% |
| Muse Spark 1.3 | 61 | 1888572 | 1742505 | 92.3% | 93.2% |
| Sonnet 5.5 | 98 | 4713740 | 4300347 | 91.2% | 92.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16317 | 441550771 | 357340162 | 80.9% | 81.2% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6677 | 236589434 | 195883536 | 82.8% | 83.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2239 | 63456962 | 58795713 | 92.7% | 93.2% |
| Sonnet 5.5 | 12670 | 394424423 | 373016592 | 94.6% | 95.2% |
