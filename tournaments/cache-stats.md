# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0084-20261108-035328)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 152 | 7160991 | 6371968 | 89.0% | 90.3% |
| GLM 5.3 Flash | 146 | 6337898 | 5660864 | 89.3% | 89.8% |
| Muse Spark 1.3 | 143 | 3945900 | 3656057 | 92.7% | 93.6% |
| Sonnet 5.5 | 240 | 13217967 | 12368616 | 93.6% | 94.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17626 | 507423285 | 416734978 | 82.1% | 82.4% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7434 | 269475686 | 225211664 | 83.6% | 84.1% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3323 | 101907213 | 94328061 | 92.6% | 93.2% |
| Sonnet 5.5 | 14331 | 487616757 | 458720992 | 94.1% | 94.7% |
