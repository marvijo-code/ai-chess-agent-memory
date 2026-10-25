# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0061-20261024-091656)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 191 | 10210774 | 8943104 | 87.6% | 87.8% |
| DeepSeek V4.1 Flash 1017 | 140 | 6210306 | 5361536 | 86.3% | 86.7% |
| GLM 5.3 Flash | 154 | 5666887 | 4371200 | 77.1% | 77.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 13339 | 283278793 | 214804224 | 75.8% | 76.1% |
| DeepSeek V4.1 Flash 1017 | 2490 | 116243234 | 102803960 | 88.4% | 88.7% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 4015 | 121831456 | 96436464 | 79.2% | 79.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
