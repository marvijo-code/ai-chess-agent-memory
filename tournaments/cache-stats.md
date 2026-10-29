# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0074-20261028-202920)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 308 | 17211538 | 15743872 | 91.5% | 91.7% |
| GLM 5.3 Flash | 337 | 16375555 | 14739136 | 90.0% | 90.3% |
| Muse Spark 1.3 | 189 | 6652817 | 6183171 | 92.9% | 93.3% |
| Sonnet 5.5 | 471 | 26795339 | 24789880 | 92.5% | 92.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15090 | 374690668 | 296982530 | 79.3% | 79.5% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5772 | 191976457 | 155907012 | 81.2% | 81.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1276 | 28819142 | 26869538 | 93.2% | 93.8% |
| Sonnet 5.5 | 11500 | 328247449 | 311843245 | 95.0% | 95.6% |
