# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0055-20261020-162203)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 112 | 5954081 | 5148800 | 86.5% | 86.6% |
| DeepSeek V4.1 Flash 1017 | 102 | 4790160 | 4256896 | 88.9% | 89.2% |
| GLM 5.3 Flash | 116 | 4932999 | 3912948 | 79.3% | 79.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 12079 | 214165707 | 153988736 | 71.9% | 72.1% |
| DeepSeek V4.1 Flash 1017 | 1299 | 60336004 | 52929252 | 87.7% | 88.0% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 2953 | 86090835 | 69743392 | 81.0% | 81.5% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
