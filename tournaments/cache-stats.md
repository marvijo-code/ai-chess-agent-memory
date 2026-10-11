# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0025-20261011-030533)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 262 | 3497058 | 1877504 | 53.7% | 53.6% |
| GPT-6.1 Sol | 116 | 2565811 | 2374912 | 92.6% | 93.3% |
| Sonnet 5.5 | 183 | 3997936 | 3820372 | 95.6% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6725 | 75393657 | 37958656 | 50.3% | 50.3% |
| GPT-6.1 Sol | 5312 | 152839235 | 142217600 | 93.1% | 93.5% |
| Sonnet 5.5 | 5627 | 124271365 | 118676401 | 95.5% | 96.1% |
