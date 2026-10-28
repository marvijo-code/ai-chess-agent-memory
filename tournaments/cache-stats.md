# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0073-20261028-121341)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 159 | 8485216 | 7454848 | 87.9% | 88.1% |
| GLM 5.3 Flash | 120 | 6226989 | 5391020 | 86.6% | 87.2% |
| Muse Spark 1.3 | 124 | 3269002 | 2981428 | 91.2% | 92.0% |
| Sonnet 5.5 | 160 | 7992200 | 7310067 | 91.5% | 92.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14696 | 353278325 | 277481730 | 78.5% | 78.8% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5435 | 175600902 | 141167876 | 80.4% | 81.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1036 | 21127209 | 19738095 | 93.4% | 94.0% |
| Sonnet 5.5 | 10901 | 293760428 | 279804977 | 95.2% | 95.9% |
