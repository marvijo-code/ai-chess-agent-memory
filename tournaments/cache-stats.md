# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0019-20261010-104326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 93 | 858835 | 330240 | 38.5% | 38.1% |
| GPT-6.1 Sol | 79 | 2334444 | 2218624 | 95.0% | 95.4% |
| Sonnet 5.5 | 96 | 2264364 | 2170312 | 95.8% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4893 | 53756101 | 25624320 | 47.7% | 47.6% |
| GPT-6.1 Sol | 3972 | 114514752 | 106378752 | 92.9% | 93.4% |
| Sonnet 5.5 | 4230 | 93332453 | 89141633 | 95.5% | 96.1% |
