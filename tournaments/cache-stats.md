# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0074-20261028-202920)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 169 | 9022791 | 8250880 | 91.4% | 91.7% |
| GLM 5.3 Flash | 195 | 10336566 | 9159872 | 88.6% | 88.9% |
| Muse Spark 1.3 | 189 | 6652817 | 6183171 | 92.9% | 93.3% |
| Sonnet 5.5 | 222 | 12321451 | 11517648 | 93.5% | 93.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14951 | 366501921 | 289489538 | 79.0% | 79.3% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5630 | 185937468 | 150327748 | 80.8% | 81.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1276 | 28819142 | 26869538 | 93.2% | 93.8% |
| Sonnet 5.5 | 11251 | 313773561 | 298571013 | 95.2% | 95.8% |
