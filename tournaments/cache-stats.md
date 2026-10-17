# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0045-20261017-034241)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 259 | 14360964 | 11863808 | 82.6% | 82.8% |
| GLM 5.3 Flash | 154 | 5823740 | 4752384 | 81.6% | 82.0% |
| GPT-6.1 Sol | 316 | 12192937 | 11506688 | 94.4% | 94.9% |
| Haiku 5.5 | 209 | 11543281 | 10974318 | 95.1% | 95.4% |
| Sonnet 5.5 | 283 | 13502059 | 12566638 | 93.1% | 93.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10783 | 149242346 | 96232064 | 64.5% | 64.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1799 | 40894792 | 34646976 | 84.7% | 85.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 533 | 27969073 | 26724590 | 95.6% | 95.9% |
| Sonnet 5.5 | 10449 | 270510027 | 258197949 | 95.4% | 96.1% |
