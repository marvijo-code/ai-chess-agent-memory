# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0053-20261020-044445)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 147 | 7396392 | 6817024 | 92.2% | 92.5% |
| DeepSeek V4.1 Flash 1017 | 82 | 2931100 | 2551464 | 87.0% | 87.7% |
| GLM 5.3 Flash | 117 | 2075135 | 1388992 | 66.9% | 68.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 11698 | 192915927 | 135278336 | 70.1% | 70.3% |
| DeepSeek V4.1 Flash 1017 | 944 | 42522211 | 37861032 | 89.0% | 89.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 2635 | 72274536 | 58735092 | 81.3% | 81.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
