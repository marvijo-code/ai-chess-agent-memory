# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0074-20261028-202920)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 87 | 5018704 | 4647040 | 92.6% | 92.9% |
| GLM 5.3 Flash | 83 | 3920913 | 3320576 | 84.7% | 85.0% |
| Muse Spark 1.3 | 52 | 2014327 | 1903890 | 94.5% | 94.9% |
| Sonnet 5.5 | 78 | 4054562 | 3754850 | 92.6% | 93.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14869 | 362497834 | 285885698 | 78.9% | 79.1% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5518 | 179521815 | 144488452 | 80.5% | 81.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1139 | 24180652 | 22590257 | 93.4% | 94.0% |
| Sonnet 5.5 | 11107 | 305506672 | 290808215 | 95.2% | 95.9% |
