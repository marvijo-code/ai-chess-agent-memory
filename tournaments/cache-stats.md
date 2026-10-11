# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0025-20261011-030533)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 309 | 3936980 | 2082816 | 52.9% | 52.9% |
| GPT-6.1 Sol | 156 | 3559689 | 3330048 | 93.5% | 94.2% |
| Sonnet 5.5 | 207 | 4334752 | 4129780 | 95.3% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6772 | 75833579 | 38163968 | 50.3% | 50.3% |
| GPT-6.1 Sol | 5352 | 153833113 | 143172736 | 93.1% | 93.5% |
| Sonnet 5.5 | 5651 | 124608181 | 118985809 | 95.5% | 96.1% |
