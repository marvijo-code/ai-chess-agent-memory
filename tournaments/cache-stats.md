# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0054-20261020-084439)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 163 | 9221128 | 8149760 | 88.4% | 88.6% |
| DeepSeek V4.1 Flash 1017 | 139 | 6694618 | 5720960 | 85.5% | 85.7% |
| GLM 5.3 Flash | 135 | 6643027 | 5274424 | 79.4% | 79.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 11913 | 205107097 | 146068608 | 71.2% | 71.4% |
| DeepSeek V4.1 Flash 1017 | 1162 | 53930676 | 47610408 | 88.3% | 88.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 2794 | 79233727 | 64191916 | 81.0% | 81.5% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
