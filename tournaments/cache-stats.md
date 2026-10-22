# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0058-20261022-100221)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 191 | 9891230 | 8730112 | 88.3% | 88.6% |
| DeepSeek V4.1 Flash 1017 | 253 | 13493783 | 12314260 | 91.3% | 91.5% |
| GLM 5.3 Flash | 136 | 2788810 | 1788524 | 64.1% | 65.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 12710 | 246544781 | 182149376 | 73.9% | 74.1% |
| DeepSeek V4.1 Flash 1017 | 2010 | 95021687 | 84357624 | 88.8% | 89.0% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 3491 | 97997097 | 78105212 | 79.7% | 80.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
