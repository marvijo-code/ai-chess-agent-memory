# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0079-20261102-080217)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 257 | 13225652 | 12143488 | 91.8% | 92.1% |
| GLM 5.3 Flash | 146 | 6111374 | 5369280 | 87.9% | 88.3% |
| Muse Spark 1.3 | 158 | 4835256 | 4458309 | 92.2% | 93.2% |
| Sonnet 5.5 | 313 | 16632158 | 15280117 | 91.9% | 92.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16497 | 450600283 | 365592066 | 81.1% | 81.4% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6768 | 240755760 | 199575120 | 82.9% | 83.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2336 | 66403646 | 61511517 | 92.6% | 93.2% |
| Sonnet 5.5 | 12885 | 406342841 | 383996362 | 94.5% | 95.1% |
