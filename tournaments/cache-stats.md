# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0071-20261027-002235)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 63 | 2957149 | 2589696 | 87.6% | 87.9% |
| GLM 5.3 Flash | 84 | 4323688 | 3974464 | 91.9% | 92.2% |
| Haiku 5.5 | 73 | 3928866 | 3651010 | 92.9% | 93.4% |
| Muse Spark 1.3 | 58 | 978498 | 905543 | 92.5% | 93.5% |
| Sonnet 5.5 | 92 | 4875531 | 4596298 | 94.3% | 94.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14247 | 329532387 | 256394754 | 77.8% | 78.1% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5000 | 154103999 | 122903164 | 79.8% | 80.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 676 | 35227030 | 33513231 | 95.1% | 95.5% |
| Muse Spark 1.3 | 613 | 10620751 | 9999101 | 94.1% | 94.7% |
| Sonnet 5.5 | 10630 | 279403236 | 266519002 | 95.4% | 96.1% |
