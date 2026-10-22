# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0058-20261022-100221)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 30 | 806133 | 663168 | 82.3% | 83.3% |
| DeepSeek V4.1 Flash 1017 | 43 | 1333119 | 1102996 | 82.7% | 83.3% |
| GLM 5.3 Flash | 38 | 861464 | 368236 | 42.7% | 43.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 12549 | 237459684 | 174082432 | 73.3% | 73.6% |
| DeepSeek V4.1 Flash 1017 | 1800 | 82861023 | 73146360 | 88.3% | 88.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 3393 | 96069751 | 76684924 | 79.8% | 80.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
