# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0060-20261022-215721)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 127 | 6740309 | 6074368 | 90.1% | 90.4% |
| DeepSeek V4.1 Flash 1017 | 103 | 4603665 | 4092544 | 88.9% | 89.2% |
| GLM 5.3 Flash | 86 | 3105178 | 1933632 | 62.3% | 63.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 13014 | 261584554 | 195053952 | 74.6% | 74.8% |
| DeepSeek V4.1 Flash 1017 | 2303 | 108304001 | 95908472 | 88.6% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 3754 | 107700538 | 85313264 | 79.2% | 79.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
