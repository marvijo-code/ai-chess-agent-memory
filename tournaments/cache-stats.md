# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0074-20261028-202920)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 137 | 7509153 | 6878080 | 91.6% | 91.9% |
| GLM 5.3 Flash | 93 | 4864537 | 4211648 | 86.6% | 86.8% |
| Muse Spark 1.3 | 101 | 3904444 | 3626095 | 92.9% | 93.2% |
| Sonnet 5.5 | 184 | 10031272 | 9366067 | 93.4% | 93.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14919 | 364988283 | 288116738 | 78.9% | 79.2% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5528 | 180465439 | 145379524 | 80.6% | 81.1% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1188 | 26070769 | 24312462 | 93.3% | 93.8% |
| Sonnet 5.5 | 11213 | 311483382 | 296419432 | 95.2% | 95.8% |
