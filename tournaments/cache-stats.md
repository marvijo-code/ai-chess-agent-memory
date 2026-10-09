# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0006-20261009-001831)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 42 | 382219 | 126720 | 33.2% | 32.5% |
| GPT-6.1 Sol | 24 | 416912 | 372736 | 89.4% | 89.9% |
| Sonnet 5.5 | 45 | 1000793 | 955323 | 95.5% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1436 | 15751810 | 7187456 | 45.6% | 45.5% |
| GPT-6.1 Sol | 1194 | 35255566 | 32968448 | 93.5% | 93.9% |
| Sonnet 5.5 | 1271 | 28990033 | 27750421 | 95.7% | 96.2% |
