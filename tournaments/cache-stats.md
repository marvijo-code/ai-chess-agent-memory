# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0077-20261101-132048)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 57 | 2968296 | 2542720 | 85.7% | 86.0% |
| GLM 5.3 Flash | 120 | 5870473 | 5177560 | 88.2% | 88.5% |
| Muse Spark 1.3 | 69 | 1785198 | 1659298 | 92.9% | 94.3% |
| Sonnet 5.5 | 54 | 2918365 | 2709869 | 92.9% | 93.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15816 | 414354283 | 332825474 | 80.3% | 80.6% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6299 | 217252656 | 178252668 | 82.0% | 82.6% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1855 | 48310698 | 44657858 | 92.4% | 93.0% |
| Sonnet 5.5 | 12105 | 361711662 | 342699885 | 94.7% | 95.4% |
