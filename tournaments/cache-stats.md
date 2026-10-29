# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0074-20261028-202920)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 293 | 16115293 | 14733568 | 91.4% | 91.7% |
| GLM 5.3 Flash | 322 | 15589483 | 14031936 | 90.0% | 90.3% |
| Muse Spark 1.3 | 189 | 6652817 | 6183171 | 92.9% | 93.3% |
| Sonnet 5.5 | 428 | 24507253 | 22689018 | 92.6% | 92.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15075 | 373594423 | 295972226 | 79.2% | 79.5% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5757 | 191190385 | 155199812 | 81.2% | 81.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1276 | 28819142 | 26869538 | 93.2% | 93.8% |
| Sonnet 5.5 | 11457 | 325959363 | 309742383 | 95.0% | 95.7% |
