# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0078-20261101-211509)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 184 | 9409895 | 8244992 | 87.6% | 87.9% |
| GLM 5.3 Flash | 243 | 13577164 | 12381544 | 91.2% | 91.5% |
| Muse Spark 1.3 | 156 | 7066891 | 6527045 | 92.4% | 92.8% |
| Sonnet 5.5 | 218 | 12569307 | 11598020 | 92.3% | 92.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16205 | 435713690 | 351970178 | 80.8% | 81.1% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6602 | 234004388 | 193643344 | 82.8% | 83.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2178 | 61568390 | 57053208 | 92.7% | 93.2% |
| Sonnet 5.5 | 12492 | 384573299 | 363897974 | 94.6% | 95.2% |
