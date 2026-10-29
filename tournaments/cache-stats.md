# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0074-20261028-202920)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 204 | 10736140 | 9764480 | 90.9% | 91.2% |
| GLM 5.3 Flash | 296 | 14699546 | 13247488 | 90.1% | 90.4% |
| Muse Spark 1.3 | 189 | 6652817 | 6183171 | 92.9% | 93.3% |
| Sonnet 5.5 | 260 | 14652035 | 13706252 | 93.5% | 94.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14986 | 368215270 | 291003138 | 79.0% | 79.3% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5731 | 190300448 | 154415364 | 81.1% | 81.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1276 | 28819142 | 26869538 | 93.2% | 93.8% |
| Sonnet 5.5 | 11289 | 316104145 | 300759617 | 95.1% | 95.8% |
