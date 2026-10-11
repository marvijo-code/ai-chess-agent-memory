# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0025-20261011-030533)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 288 | 3693775 | 1962496 | 53.1% | 53.1% |
| GPT-6.1 Sol | 156 | 3559689 | 3330048 | 93.5% | 94.2% |
| Sonnet 5.5 | 198 | 4155519 | 3959423 | 95.3% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6751 | 75590374 | 38043648 | 50.3% | 50.3% |
| GPT-6.1 Sol | 5352 | 153833113 | 143172736 | 93.1% | 93.5% |
| Sonnet 5.5 | 5642 | 124428948 | 118815452 | 95.5% | 96.1% |
