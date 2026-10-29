# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0075-20261029-072421)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 106 | 5472887 | 4923648 | 90.0% | 90.2% |
| GLM 5.3 Flash | 56 | 1836992 | 1525376 | 83.0% | 83.6% |
| Muse Spark 1.3 | 126 | 3929405 | 3550501 | 90.4% | 90.8% |
| Sonnet 5.5 | 86 | 4742822 | 4451741 | 93.9% | 94.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15220 | 380996834 | 302651778 | 79.4% | 79.7% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5851 | 194487376 | 158023172 | 81.3% | 81.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1402 | 32748547 | 30420039 | 92.9% | 93.4% |
| Sonnet 5.5 | 11586 | 332990271 | 316294986 | 95.0% | 95.6% |
