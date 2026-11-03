# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0081-20261103-045347)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 161 | 8028779 | 7367680 | 91.8% | 92.2% |
| GLM 5.3 Flash | 164 | 7733162 | 6929472 | 89.6% | 90.0% |
| Muse Spark 1.3 | 119 | 3231416 | 2675673 | 82.8% | 83.7% |
| Sonnet 5.5 | 202 | 10643900 | 9743974 | 91.5% | 92.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16912 | 471762929 | 384766978 | 81.6% | 81.8% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7039 | 252601752 | 210083024 | 83.2% | 83.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2637 | 75297026 | 69392704 | 92.2% | 92.8% |
| Sonnet 5.5 | 13306 | 427968563 | 403560375 | 94.3% | 94.9% |
