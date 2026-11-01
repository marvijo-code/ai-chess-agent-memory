# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0078-20261101-211509)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 66 | 3617914 | 3331712 | 92.1% | 92.4% |
| GLM 5.3 Flash | 30 | 1040457 | 970944 | 93.3% | 93.9% |
| Muse Spark 1.3 | 12 | 178143 | 154316 | 86.6% | 90.2% |
| Sonnet 5.5 | 73 | 4553877 | 4290627 | 94.2% | 94.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16087 | 429921709 | 347056898 | 80.7% | 81.0% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6389 | 221467681 | 182232744 | 82.3% | 82.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2034 | 54679642 | 50680479 | 92.7% | 93.3% |
| Sonnet 5.5 | 12347 | 376557869 | 356590581 | 94.7% | 95.3% |
