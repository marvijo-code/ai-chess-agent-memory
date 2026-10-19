# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0050-20261019-102456)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 135 | 6100410 | 5283456 | 86.6% | 87.0% |
| DeepSeek V4.1 Flash 1017 | 142 | 6504217 | 5838208 | 89.8% | 90.0% |
| GLM 5.3 Flash | 174 | 9558455 | 7637124 | 79.9% | 80.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 11052 | 159407267 | 104923264 | 65.8% | 66.0% |
| DeepSeek V4.1 Flash 1017 | 392 | 17162737 | 15438592 | 90.0% | 90.2% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 2148 | 57799187 | 48048004 | 83.1% | 83.6% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
