# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0086-20261108-185025)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 246 | 14546001 | 13596544 | 93.5% | 94.0% |
| GLM 5.3 Flash | 207 | 10298889 | 9580928 | 93.0% | 93.3% |
| Muse Spark 1.3 | 160 | 6351282 | 5800374 | 91.3% | 91.7% |
| Sonnet 5.5 | 249 | 14492813 | 13642280 | 94.1% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18125 | 536367935 | 443745794 | 82.7% | 83.1% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7854 | 288841189 | 243073360 | 84.2% | 84.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3747 | 117291866 | 108534285 | 92.5% | 93.1% |
| Sonnet 5.5 | 14914 | 520454109 | 489541252 | 94.1% | 94.6% |
